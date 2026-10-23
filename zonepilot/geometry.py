"""Bounded planar WGS84 geometry and great-circle distance, using only stdlib.

Membership includes every ring boundary within 1e-9 degrees of a segment.
Validation rejects touching or nearly touching rings and components because
their topology is ambiguous at that tolerance. Winding is immaterial. The
20,000-position cap includes closing positions; the 32-ring cap covers the
entire geometry. A tolerance-aware x sweep bounds segment-pair work to
2,000,000 candidates across all rings, failing closed if that budget is exceeded.
Validation takes O(V log V + C + R*V) time and O(V) space, where C is the
budgeted number of x-overlapping segment pairs.
"""

import heapq
import math

__all__ = [
    "GeometryError",
    "validate_geometry",
    "contains",
    "bounds",
    "haversine",
    "valid_point",
]

_TOLERANCE = 1e-9
_MAX_VERTICES = 20_000
_MAX_RINGS = 32
_MAX_CANDIDATE_PAIRS = 2_000_000
_EARTH_RADIUS_METRES = 6_371_008.8

type Point = tuple[float, float]
type Ring = list[Point]
type Polygon = list[Ring]


class GeometryError(ValueError):
    """An invalid or unsupported geometry, without untrusted input details."""

    code = "unsupported_geometry"

    def __init__(self, *_details):
        super().__init__("Unsupported or invalid geometry.")


def valid_point(value, max_lat=90) -> bool:
    """Whether value is exactly two finite JSON numbers in lon/lat order."""
    if (
        not isinstance(max_lat, (int, float))
        or isinstance(max_lat, bool)
        or not 0 <= max_lat <= 90
        or not isinstance(value, (list, tuple))
        or len(value) != 2
    ):
        return False
    lon, lat = value
    # Range checks also reject infinities, NaN, and huge integers without
    # converting arbitrary-size integers to floats.
    return (
        isinstance(lon, (int, float))
        and not isinstance(lon, bool)
        and isinstance(lat, (int, float))
        and not isinstance(lat, bool)
        and -180 <= lon <= 180
        and -max_lat <= lat <= max_lat
    )


def _polygons(geometry):
    coordinates = geometry["coordinates"]
    return [coordinates] if geometry["type"] == "Polygon" else coordinates


def _on_segment(point: Point, start: Point, end: Point) -> bool:
    """Use distance to the finite segment, with an expanded bounding box."""
    x, y = point
    ax, ay = start
    bx, by = end
    if (
        x < min(ax, bx) - _TOLERANCE
        or x > max(ax, bx) + _TOLERANCE
        or y < min(ay, by) - _TOLERANCE
        or y > max(ay, by) + _TOLERANCE
    ):
        return False
    dx, dy = bx - ax, by - ay
    length_squared = dx * dx + dy * dy
    if length_squared == 0:
        return math.hypot(x - ax, y - ay) <= _TOLERANCE
    along = max(0.0, min(1.0, ((x - ax) * dx + (y - ay) * dy) / length_squared))
    return math.hypot(x - (ax + along * dx), y - (ay + along * dy)) <= _TOLERANCE


def _turn(a: Point, b: Point, c: Point) -> int:
    left = (b[0] - a[0]) * (c[1] - a[1])
    right = (b[1] - a[1]) * (c[0] - a[0])
    determinant = left - right
    # Treat cancellation near floating-point roundoff as indeterminate.
    uncertainty = 8 * (math.ulp(left) + math.ulp(right))
    if abs(determinant) <= uncertainty:
        return 0
    return 1 if determinant > 0 else -1


def _segments_contact(a: Point, b: Point, c: Point, d: Point) -> bool:
    if (
        max(a[0], b[0]) + _TOLERANCE < min(c[0], d[0])
        or max(c[0], d[0]) + _TOLERANCE < min(a[0], b[0])
        or max(a[1], b[1]) + _TOLERANCE < min(c[1], d[1])
        or max(c[1], d[1]) + _TOLERANCE < min(a[1], b[1])
    ):
        return False
    turns = (_turn(a, b, c), _turn(a, b, d), _turn(c, d, a), _turn(c, d, b))
    if turns[0] * turns[1] < 0 and turns[2] * turns[3] < 0:
        return True
    if (
        _on_segment(a, c, d)
        or _on_segment(b, c, d)
        or _on_segment(c, a, b)
        or _on_segment(d, a, b)
    ):
        return True
    # Near-collinearity within the bounded coordinate range is covered by the
    # distance checks above. A collinear endpoint beyond a segment is harmless.
    return False


def _ring_location(ring, point) -> int:
    """Return -1 outside, 0 on the boundary, or 1 strictly inside."""
    inside = False
    x, y = point
    for start, end in zip(ring, ring[1:]):
        if _on_segment(point, start, end):
            return 0
        ax, ay = start
        bx, by = end
        if (ay > y) != (by > y) and x < ax + (y - ay) * (bx - ax) / (by - ay):
            inside = not inside
    return 1 if inside else -1


def _polygon_contains(polygon, point) -> bool:
    exterior = _ring_location(polygon[0], point)
    if exterior <= 0:
        return exterior == 0
    for hole in polygon[1:]:
        location = _ring_location(hole, point)
        if location == 0:
            return True
        if location == 1:
            return False
    return True


def _validate_ring(ring: Ring) -> None:
    vertices = ring[:-1]
    if ring[0] != ring[-1] or len(set(vertices)) != len(vertices):
        raise GeometryError()
    perimeter = 0.0
    origin_x, origin_y = ring[0]
    areas = []
    for index, (start, end) in enumerate(zip(ring, ring[1:])):
        length = math.hypot(end[0] - start[0], end[1] - start[1])
        if length <= _TOLERANCE or abs(end[0] - start[0]) > 180:
            raise GeometryError()
        perimeter += length
        areas.append(
            (start[0] - origin_x) * (end[1] - origin_y)
            - (end[0] - origin_x) * (start[1] - origin_y)
        )
        following = vertices[(index + 2) % len(vertices)]
        if _on_segment(start, end, following) or _on_segment(following, start, end):
            raise GeometryError()
    if abs(math.fsum(areas)) <= _TOLERANCE * perimeter:
        raise GeometryError()


def _validate_segment_contacts(rings: list[Ring]) -> None:
    """Check all rings together; count even y-disjoint and adjacent candidates.

    Expiration uses exactly the x tolerance in _segments_contact. Each active
    pair is visited once, including long edges spanning many later start events.
    The heap avoids unbudgeted repeated scans just to expire active edges.
    """
    edges = []
    for ring_index, ring in enumerate(rings):
        for edge_index, (a, b) in enumerate(zip(ring, ring[1:])):
            edges.append((min(a[0], b[0]), max(a[0], b[0]),
                          min(a[1], b[1]), max(a[1], b[1]),
                          ring_index, edge_index, a, b))
    edges.sort(key=lambda edge: edge[0])
    active = {}
    expirations = []
    candidates = 0
    for identifier, edge in enumerate(edges):
        min_x, max_x, min_y, max_y, ring_index, edge_index, a, b = edge
        while expirations and expirations[0][0] + _TOLERANCE < min_x:
            _, expired = heapq.heappop(expirations)
            del active[expired]
        for other in active.values():
            candidates += 1
            if candidates > _MAX_CANDIDATE_PAIRS:
                raise GeometryError()
            _, _, other_min_y, other_max_y, other_ring, other_index, c, d = other
            if max_y + _TOLERANCE < other_min_y or other_max_y + _TOLERANCE < min_y:
                continue
            if ring_index == other_ring and abs(edge_index - other_index) in (
                1, len(rings[ring_index]) - 2
            ):
                # Adjacent edges share a vertex. _validate_ring separately
                # rejects their backtracking, short edges and degeneracy.
                continue
            if _segments_contact(a, b, c, d):
                raise GeometryError()
        active[identifier] = edge
        heapq.heappush(expirations, (max_x, identifier))


def validate_geometry(geojson):
    """Validate a bare Polygon/MultiPolygon and return the identical object.

    Coordinates must be lon/lat pairs, with latitudes in [-85, 85]. Longitude
    edges and the full geometry's span may not exceed 180 degrees. Rings must
    be simple, nondegenerate, closed and strictly nested as exterior/holes.
    Holes cannot touch, overlap or contain one another. Components cannot
    touch or overlap; an island strictly inside another component's hole is
    allowed. Legacy CRS declarations are unsupported. No input is modified.
    """
    if (
        not isinstance(geojson, dict)
        or geojson.get("type") not in ("Polygon", "MultiPolygon")
        or "crs" in geojson
    ):
        raise GeometryError()
    coordinates = geojson.get("coordinates")
    if not isinstance(coordinates, (list, tuple)) or not coordinates:
        raise GeometryError()
    polygons = _polygons(geojson)
    if len(polygons) > _MAX_RINGS:
        raise GeometryError()
    ring_count = vertex_count = 0
    normalized: list[Polygon] = []
    all_rings: list[Ring] = []
    for polygon in polygons:
        if not isinstance(polygon, (list, tuple)) or not polygon:
            raise GeometryError()
        ring_count += len(polygon)
        if ring_count > _MAX_RINGS:
            raise GeometryError()
        normalized_polygon = []
        for ring in polygon:
            if not isinstance(ring, (list, tuple)) or len(ring) < 4:
                raise GeometryError()
            vertex_count += len(ring)
            if vertex_count > _MAX_VERTICES:
                raise GeometryError()
            if any(not valid_point(point, max_lat=85) for point in ring):
                raise GeometryError()
            points = [(float(point[0]), float(point[1])) for point in ring]
            normalized_polygon.append(points)
            all_rings.append(points)
        normalized.append(normalized_polygon)

    longitudes = [point[0] for ring in all_rings for point in ring]
    if max(longitudes) - min(longitudes) > 180:
        raise GeometryError()
    # Establish structural limits before topology work begins.
    for ring in all_rings:
        _validate_ring(ring)
    _validate_segment_contacts(all_rings)
    for polygon in normalized:
        for index, hole in enumerate(polygon[1:], start=1):
            if _ring_location(polygon[0], hole[0]) != 1:
                raise GeometryError()
            for other in polygon[index + 1:]:
                if (
                    _ring_location(hole, other[0]) != -1
                    or _ring_location(other, hole[0]) != -1
                ):
                    raise GeometryError()
    for index, polygon in enumerate(normalized):
        for other in normalized[index + 1:]:
            if _polygon_contains(polygon, other[0][0]) or _polygon_contains(
                other, polygon[0][0]
            ):
                raise GeometryError()
    return geojson


def contains(geometry, point) -> bool:
    """Test a point against an already validated, subsequently unmodified zone."""
    if not valid_point(point):
        return False
    return any(_polygon_contains(polygon, point) for polygon in _polygons(geometry))


def bounds(geometry) -> list[float]:
    """Return [minlon, minlat, maxlon, maxlat] for validated geometry."""
    points = [
        point for polygon in _polygons(geometry) for ring in polygon for point in ring
    ]
    return [
        min(point[0] for point in points),
        min(point[1] for point in points),
        max(point[0] for point in points),
        max(point[1] for point in points),
    ]


def haversine(a, b) -> float:
    """Great-circle metres between WGS84 lon/lat pairs, using mean Earth radius."""
    if not valid_point(a) or not valid_point(b):
        raise GeometryError()
    lat_a, lat_b = math.radians(a[1]), math.radians(b[1])
    delta_lat = lat_b - lat_a
    delta_lon = math.radians(math.remainder(b[0] - a[0], 360))
    half_chord = (
        math.sin(delta_lat / 2) ** 2
        + math.cos(lat_a) * math.cos(lat_b) * math.sin(delta_lon / 2) ** 2
    )
    half_chord = max(0.0, min(1.0, half_chord))
    return _EARTH_RADIUS_METRES * 2 * math.atan2(
        math.sqrt(half_chord), math.sqrt(1 - half_chord)
    )
