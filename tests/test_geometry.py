"""Authored synthetic geometry tests; no API recordings or network access."""

import copy
import itertools
import math
import unittest
from unittest.mock import patch

from zonepilot.geometry import (
    GeometryError,
    bounds,
    contains,
    haversine,
    valid_point,
    validate_geometry,
)


def rectangle(left=0, bottom=0, right=10, top=10):
    return [[left, bottom], [right, bottom], [right, top], [left, top], [left, bottom]]


def polygon(*rings):
    return {"type": "Polygon", "coordinates": list(rings) or [rectangle()]}


def multipolygon(*polygons):
    return {"type": "MultiPolygon", "coordinates": list(polygons)}


def regular_ring(vertices):
    points = [
        [10 * math.cos(2 * math.pi * i / vertices), 10 * math.sin(2 * math.pi * i / vertices)]
        for i in range(vertices)
    ]
    return points + [points[0][:]]


class PointTests(unittest.TestCase):
    def test_valid_lon_lat_pairs(self):
        for point in ([0, 0], [-180, -90], [180, 90], (12.5, -47.25), [-0.0, 0.0]):
            with self.subTest(point=point):
                self.assertIs(valid_point(point), True)

    def test_invalid_shape_types_ranges_and_nonfinite_values(self):
        invalid = [
            None, {}, "12", 12, [], [1], [1, 2, 3], {1, 2},
            [True, 0], [0, False], ["1", 2], [1, None], [1j, 0],
            [180.00001, 0], [-180.00001, 0], [0, 90.00001], [0, -90.00001],
            [math.inf, 0], [-math.inf, 0], [math.nan, 0],
            [0, math.inf], [0, -math.inf], [0, math.nan], [10**1000, 0],
        ]
        for index, point in enumerate(invalid):
            with self.subTest(case=index):
                self.assertIs(valid_point(point), False)

    def test_latitude_limit_is_explicit_and_inclusive(self):
        self.assertTrue(valid_point([170, 85], max_lat=85))
        self.assertTrue(valid_point([-170, -85], max_lat=85))
        self.assertFalse(valid_point([12, 85.00001], max_lat=85))
        self.assertFalse(valid_point([12, -85.00001], max_lat=85))
        self.assertTrue(valid_point([0, 0], max_lat=0))
        for limit in (True, None, "85", -1, 91, math.nan, math.inf):
            with self.subTest(limit=limit):
                self.assertFalse(valid_point([0, 0], max_lat=limit))


class MembershipTests(unittest.TestCase):
    def test_validation_preserves_object_coordinates_and_metadata(self):
        geometry = polygon(rectangle(), rectangle(2, 2, 4, 4))
        geometry["synthetic"] = True
        original = copy.deepcopy(geometry)
        self.assertIs(validate_geometry(geometry), geometry)
        self.assertTrue(contains(geometry, [1, 1]))
        self.assertEqual(bounds(geometry), [0, 0, 10, 10])
        self.assertEqual(geometry, original)

    def test_polygon_interior_and_exterior(self):
        geometry = validate_geometry(polygon())
        for point, expected in (([5, 5], True), ([-1, 5], False), ([5, 11], False)):
            with self.subTest(point=point):
                self.assertIs(contains(geometry, point), expected)

    def test_every_exterior_and_hole_vertex_and_edge_is_in_zone(self):
        rings = [rectangle(), rectangle(2, 2, 4, 4), rectangle(6, 6, 8, 8)]
        geometry = validate_geometry(polygon(*rings))
        for ring_index, ring in enumerate(rings):
            for start, end in zip(ring, ring[1:]):
                midpoint = [(a + b) / 2 for a, b in zip(start, end)]
                with self.subTest(ring=ring_index, start=start):
                    self.assertTrue(contains(geometry, start))
                    self.assertTrue(contains(geometry, midpoint))
        self.assertFalse(contains(geometry, [3, 3]))
        self.assertFalse(contains(geometry, [7, 7]))
        self.assertTrue(contains(geometry, [5, 5]))

    def test_winding_does_not_change_any_verdict(self):
        rings = [rectangle(), rectangle(2, 2, 4, 4), rectangle(6, 6, 8, 8)]
        for reversals in itertools.product((False, True), repeat=3):
            geometry = validate_geometry(polygon(*[
                ring[::-1] if reverse else ring
                for ring, reverse in zip(rings, reversals)
            ]))
            for point, expected in (([1, 1], True), ([3, 3], False), ([7, 7], False),
                                    ([2, 3], True), ([0, 0], True), ([11, 5], False)):
                with self.subTest(reversals=reversals, point=point):
                    self.assertIs(contains(geometry, point), expected)

    def test_concave_polygon_uses_shape_rather_than_bounding_box(self):
        ring = [[0, 0], [8, 0], [8, 8], [6, 8], [6, 2], [2, 2], [2, 8], [0, 8], [0, 0]]
        geometry = validate_geometry(polygon(ring))
        for point, expected in (([1, 5], True), ([7, 5], True), ([4, 1], True),
                                ([4, 5], False), ([4, 2], True), ([9, 5], False)):
            with self.subTest(point=point):
                self.assertIs(contains(geometry, point), expected)

    def test_collinear_forward_vertices_are_valid(self):
        geometry = validate_geometry(polygon([[0, 0], [1, 0], [2, 0], [0, 2], [0, 0]]))
        self.assertTrue(contains(geometry, [1, 0.5]))
        self.assertTrue(contains(geometry, [1.5, 0]))

    def test_ray_through_vertex_does_not_double_count(self):
        geometry = validate_geometry(polygon([[0, 2], [2, 0], [4, 2], [2, 4], [0, 2]]))
        self.assertTrue(contains(geometry, [2, 2]))
        self.assertFalse(contains(geometry, [-1, 2]))
        self.assertFalse(contains(geometry, [5, 2]))

    def test_tolerance_includes_nearby_boundary_points_on_both_sides(self):
        geometry = validate_geometry(polygon())
        for point in ([5, -1e-9], [5, -0.5e-9], [-0.5e-9, 5], [10 + 0.5e-9, 5]):
            with self.subTest(point=point):
                self.assertTrue(contains(geometry, point))
        for point in ([5, -2e-9], [-2e-9, 5], [10 + 2e-9, 5]):
            with self.subTest(point=point):
                self.assertFalse(contains(geometry, point))

    def test_hole_tolerance_excludes_only_strict_interior_beyond_tolerance(self):
        geometry = validate_geometry(polygon(rectangle(), rectangle(2, 2, 4, 4)))
        for point in ([3, 2 + 0.5e-9], [3, 2 - 0.5e-9], [2 + 0.5e-9, 3]):
            with self.subTest(point=point):
                self.assertTrue(contains(geometry, point))
        self.assertFalse(contains(geometry, [3, 2 + 2e-9]))
        self.assertFalse(contains(geometry, [2 + 2e-9, 3]))

    def test_diagonal_tolerance_is_euclidean_distance(self):
        geometry = validate_geometry(polygon([[0, 0], [10, 0], [0, 10], [0, 0]]))
        near = 0.5e-9 / math.sqrt(2)
        far = 2e-9 / math.sqrt(2)
        self.assertTrue(contains(geometry, [5 + near, 5 + near]))
        self.assertFalse(contains(geometry, [5 + far, 5 + far]))

    def test_segment_endpoint_tolerance_uses_circle_with_expanded_box(self):
        geometry = validate_geometry(polygon())
        self.assertTrue(contains(geometry, [-0.6e-9, -0.6e-9]))
        self.assertFalse(contains(geometry, [-0.8e-9, -0.8e-9]))
        self.assertFalse(contains(geometry, [-2e-9, 0]))

    def test_short_segment_tolerance_is_not_an_unscaled_cross_product(self):
        geometry = validate_geometry(polygon(rectangle(0, 0, 1e-4, 1e-4)))
        self.assertTrue(contains(geometry, [5e-5, -0.5e-9]))
        self.assertFalse(contains(geometry, [5e-5, -1e-6]))

    def test_multipolygon_union_retains_holes_and_disconnected_components(self):
        geometry = validate_geometry(multipolygon(
            [rectangle(), rectangle(2, 2, 4, 4)], [rectangle(20, -5, 30, 5)]
        ))
        for point, expected in (([1, 1], True), ([3, 3], False), ([2, 3], True),
                                ([25, 0], True), ([20, 0], True), ([15, 0], False)):
            with self.subTest(point=point):
                self.assertIs(contains(geometry, point), expected)
        self.assertEqual(bounds(geometry), [0, -5, 30, 10])

    def test_island_component_inside_hole_is_valid_in_any_order_or_winding(self):
        shell = [rectangle(), rectangle(2, 2, 8, 8)]
        island = [rectangle(3, 3, 4, 4)]
        for reverse in (False, True):
            for components in ((shell, island), (island, shell)):
                geometry = validate_geometry(multipolygon(*[
                    [ring[::-1] if reverse else ring for ring in component]
                    for component in components
                ]))
                self.assertTrue(contains(geometry, [3.5, 3.5]))
                self.assertFalse(contains(geometry, [6, 6]))
                self.assertTrue(contains(geometry, [3, 3]))

    def test_disjoint_components_with_overlapping_bounding_boxes(self):
        first = [[0, 0], [4, 0], [0, 4], [0, 0]]
        second = [[4, 4], [4, 1], [1, 4], [4, 4]]
        geometry = validate_geometry(multipolygon([first], [second]))
        self.assertTrue(contains(geometry, [0.5, 0.5]))
        self.assertTrue(contains(geometry, [3.5, 3.5]))
        self.assertFalse(contains(geometry, [2.25, 2.25]))

    def test_coordinates_remain_lon_lat(self):
        geometry = validate_geometry(polygon(rectangle(120, 20, 125, 25)))
        self.assertTrue(contains(geometry, [121, 23]))
        self.assertFalse(contains(geometry, [23, 121]))
        self.assertEqual(bounds(geometry), [120, 20, 125, 25])

    def test_invalid_query_point_is_false(self):
        geometry = validate_geometry(polygon())
        for point in (None, [True, 1], [1, math.nan], [1, 2, 3], [181, 0]):
            with self.subTest(point=point):
                self.assertIs(contains(geometry, point), False)

    def test_query_does_not_repeat_topology_validation(self):
        geometry = validate_geometry(polygon())
        with patch("zonepilot.geometry.validate_geometry", side_effect=AssertionError):
            self.assertTrue(contains(geometry, [1, 1]))
            self.assertEqual(bounds(geometry), [0, 0, 10, 10])

    def test_tuple_containers_and_mixed_numeric_closure(self):
        ring = ((0, 0), (10.0, 0), (10, 10), (0, 10.0), (0.0, 0.0))
        geometry = {"type": "Polygon", "coordinates": (ring,)}
        self.assertIs(validate_geometry(geometry), geometry)
        self.assertTrue(contains(geometry, (1.0, 1)))


class ValidationTests(unittest.TestCase):
    def assert_invalid(self, geometry):
        with self.assertRaises(GeometryError) as caught:
            validate_geometry(geometry)
        self.assertIsInstance(caught.exception, ValueError)
        self.assertEqual(str(caught.exception), "Unsupported or invalid geometry.")
        self.assertIsNone(caught.exception.__cause__)

    def test_unsupported_geometry_types_and_envelopes(self):
        for geometry in (None, [], "Polygon", {}, {"coordinates": []},
                         {"type": "Point", "coordinates": [1, 2]},
                         {"type": "LineString", "coordinates": rectangle()},
                         {"type": "GeometryCollection", "geometries": []},
                         {"type": "Feature", "geometry": polygon()},
                         {"type": "FeatureCollection", "features": []},
                         {"type": "polygon", "coordinates": [rectangle()]},
                         {"type": [], "coordinates": []}):
            with self.subTest(geometry=geometry):
                self.assert_invalid(geometry)

    def test_crs_declarations_are_unsupported(self):
        geometry = polygon()
        geometry["crs"] = {"type": "name", "properties": {"name": "synthetic-crs"}}
        self.assert_invalid(geometry)

    def test_missing_empty_and_malformed_coordinate_nesting(self):
        for kind, coordinates in itertools.product(
            ("Polygon", "MultiPolygon"), (None, [], {}, "synthetic", [None], [[]], [[[]]])
        ):
            with self.subTest(kind=kind, coordinates=coordinates):
                self.assert_invalid({"type": kind, "coordinates": coordinates})
        self.assert_invalid({"type": "Polygon"})
        self.assert_invalid({"type": "Polygon", "coordinates": rectangle()})
        self.assert_invalid({"type": "MultiPolygon", "coordinates": [rectangle()]})

    def test_invalid_coordinate_values(self):
        values = ([1, 2, 3], [1], "synthetic", [True, 1], [1, False], [None, 1],
                  ["synthetic-detail", 1], [math.nan, 1], [1, math.inf],
                  [-181, 1], [181, 1], [1, 85.00001], [1, -85.00001], [10**1000, 1])
        for index, point in enumerate(values):
            geometry = polygon()
            geometry["coordinates"][0][1] = point
            with self.subTest(case=index):
                self.assert_invalid(geometry)

    def test_exact_ring_closure_and_at_least_three_distinct_vertices(self):
        for ring in ([], [[0, 0]], [[0, 0], [1, 1], [0, 0]],
                     [[0, 0], [1, 0], [1, 1], [0, 1]],
                     [[0, 0], [1, 0], [1, 1], [1e-12, 0]],
                     [[0, 0], [1, 1], [0, 0], [0, 0]]):
            with self.subTest(ring=ring):
                self.assert_invalid(polygon(ring))

    def test_degenerate_repeated_backtracking_and_self_intersecting_rings(self):
        rings = [
            [[0, 0], [1, 0], [2, 0], [0, 0]],
            [[0, 0], [2, 0], [2, 0], [0, 2], [0, 0]],
            [[0, 0], [3, 0], [1, 0], [1, 3], [0, 3], [0, 0]],
            [[0, 0], [3, 3], [0, 3], [3, 0], [0, 0]],
            [[0, 0], [4, 4], [0, 5], [5, 0], [0, 0]],
            [[0, 0], [4, 0], [4, 4], [2, 0], [0, 4], [0, 0]],
            [[0, 0], [4, 0], [4, 4], [2, 2], [0, 4], [2, 2], [0, 0]],
            [[0, 0], [4, 0], [4, 4], [1, 0], [3, 0], [0, 4], [0, 0]],
            [[0, 0], [0.5e-9, 0], [1, 1], [0, 1], [0, 0]],
            rectangle(0, 0, 1, 0.5e-9),
        ]
        for index, ring in enumerate(rings):
            with self.subTest(case=index):
                self.assert_invalid(polygon(ring))

    def test_holes_must_be_strictly_inside_exterior(self):
        holes = [rectangle(20, 20, 22, 22), rectangle(8, 2, 12, 4),
                 rectangle(0, 2, 2, 4), rectangle(0, 0, 2, 2), rectangle(),
                 rectangle(-1, -1, 11, 11), rectangle(0.5e-9, 2, 2, 4)]
        for index, hole in enumerate(holes):
            with self.subTest(case=index):
                self.assert_invalid(polygon(rectangle(), hole))

    def test_hole_cannot_escape_concave_exterior_without_vertex_outside(self):
        outer = [[0, 0], [8, 0], [8, 8], [6, 8], [6, 2], [2, 2], [2, 8], [0, 8], [0, 0]]
        self.assert_invalid(polygon(outer, rectangle(1, 1, 7, 7)))

    def test_holes_cannot_overlap_touch_or_nest(self):
        first = rectangle(2, 2, 5, 5)
        for second in (rectangle(4, 4, 7, 7), rectangle(5, 2, 7, 4),
                       rectangle(5, 5, 7, 7), rectangle(3, 3, 4, 4),
                       rectangle(1, 1, 6, 6), first,
                       rectangle(5 + 0.5e-9, 2, 7, 4)):
            with self.subTest(second=second):
                self.assert_invalid(polygon(rectangle(), first, second))

    def test_components_cannot_cross_contain_coincide_or_touch(self):
        first = rectangle(0, 0, 5, 5)
        for second in (rectangle(4, 4, 8, 8), rectangle(1, 1, 2, 2),
                       rectangle(-1, -1, 6, 6), first, rectangle(5, 0, 8, 5),
                       rectangle(5, 5, 8, 8), rectangle(5 + 0.5e-9, 0, 8, 5)):
            for components in (([first], [second]), ([second], [first])):
                with self.subTest(second=second, components=components):
                    self.assert_invalid(multipolygon(*components))

    def test_component_inside_shell_with_hole_still_overlaps(self):
        self.assert_invalid(multipolygon(
            [rectangle(), rectangle(2, 2, 4, 4)], [rectangle(5, 5, 6, 6)]
        ))

    def test_component_touching_or_crossing_hole_is_rejected(self):
        for island in (rectangle(2, 3, 4, 4), rectangle(1, 3, 4, 4), rectangle(1, 1, 9, 9)):
            with self.subTest(island=island):
                self.assert_invalid(multipolygon(
                    [rectangle(), rectangle(2, 2, 8, 8)], [island]
                ))

    def test_longitude_spans_edges_and_antimeridian_are_rejected(self):
        geometries = [
            polygon(rectangle(-179, 0, 179, 1)),
            polygon([[-170, 0], [0, 0], [170, 1], [0, 2], [-170, 0]]),
            multipolygon([rectangle(-179, 0, -178, 1)], [rectangle(178, 0, 179, 1)]),
            polygon(rectangle(-180, 0, 180, 1)),
        ]
        for geometry in geometries:
            with self.subTest(geometry=geometry):
                self.assert_invalid(geometry)

    def test_supported_longitude_and_latitude_extremes_are_inclusive(self):
        for ring in (rectangle(-90, -85, 90, 85), rectangle(179, 0, 180, 1),
                     rectangle(-180, 0, -179, 1)):
            with self.subTest(ring=ring):
                geometry = validate_geometry(polygon(ring))
                self.assertTrue(contains(geometry, ring[0]))

    def test_vertex_cap_includes_closing_positions(self):
        geometry = polygon(regular_ring(1999))
        self.assertIs(validate_geometry(geometry), geometry)
        self.assertTrue(contains(geometry, [0, 0]))
        self.assert_invalid(polygon(regular_ring(2000)))

    def test_vertex_cap_applies_across_components(self):
        first = regular_ring(1000)
        second = [[x + 30, y] for x, y in regular_ring(1000)]
        self.assert_invalid(multipolygon([first], [second]))

    def test_ring_cap_applies_across_components_and_holes(self):
        components = [[rectangle(3 * i, 0, 3 * i + 1, 1)] for i in range(32)]
        self.assertIsNotNone(validate_geometry(multipolygon(*components)))
        self.assert_invalid(multipolygon(*components, [rectangle(100, 0, 101, 1)]))
        holes = [rectangle(2 * i + 1, 1, 2 * i + 2, 2) for i in range(31)]
        self.assertIsNotNone(validate_geometry(polygon(rectangle(0, 0, 70, 3), *holes)))
        self.assert_invalid(polygon(rectangle(0, 0, 70, 3), *holes, rectangle(65, 1, 66, 2)))

    def test_complexity_caps_are_checked_before_quadratic_topology(self):
        oversized = [
            polygon(regular_ring(2000)),
            multipolygon(*[[rectangle(2 * i, 0, 2 * i + 1, 1)] for i in range(33)]),
            polygon(rectangle(), *[rectangle(1, 1, 2, 2) for _ in range(32)]),
        ]
        with patch("zonepilot.geometry._validate_ring", side_effect=AssertionError):
            for geometry in oversized:
                self.assert_invalid(geometry)

    def test_error_message_never_contains_untrusted_details(self):
        self.assertEqual(str(GeometryError("synthetic-private-detail")),
                         "Unsupported or invalid geometry.")
        geometry = polygon()
        geometry["coordinates"][0][1] = ["synthetic-private-detail", 0]
        self.assert_invalid(geometry)


class HaversineTests(unittest.TestCase):
    def test_identical_points_and_equivalent_antimeridian_are_zero(self):
        self.assertEqual(haversine([12, 34], [12, 34]), 0.0)
        self.assertEqual(haversine([-180, 10], [180, 10]), 0.0)

    def test_equatorial_degree_and_quarter_circumference(self):
        radius = 6_371_008.8
        self.assertAlmostEqual(haversine([0, 0], [1, 0]), radius * math.pi / 180, places=7)
        self.assertAlmostEqual(haversine([0, 0], [90, 0]), radius * math.pi / 2, places=7)

    def test_lon_lat_order_matches_independent_spherical_cosine(self):
        # At latitude 60, a longitude difference of 90 has central-angle cosine 3/4.
        expected = 6_371_008.8 * math.acos(0.75)
        self.assertAlmostEqual(haversine([10, 60], [100, 60]), expected, places=7)

    def test_antimeridian_distance_takes_short_arc(self):
        expected = 6_371_008.8 * math.pi / 90
        self.assertAlmostEqual(haversine([179, 0], [-179, 0]), expected, places=7)

    def test_antipodal_polar_and_nearly_antipodal_points_are_finite(self):
        radius = 6_371_008.8
        for a, b in (([0, 0], [180, 0]), ([0, -90], [0, 90]),
                     ([10, 30], [-170, -30]), ([0, 0], [179.999999999, 0])):
            with self.subTest(a=a, b=b):
                distance = haversine(a, b)
                self.assertTrue(math.isfinite(distance))
                self.assertLessEqual(distance, radius * math.pi)
                self.assertAlmostEqual(distance, radius * math.pi, places=6)

    def test_distance_is_symmetric_and_small_distances_remain_positive(self):
        a, b = [-12.5, 34.25], [23.75, -45.5]
        self.assertAlmostEqual(haversine(a, b), haversine(b, a), places=7)
        self.assertGreater(haversine([0, 0], [1e-12, 0]), 0)

    def test_invalid_distance_points_raise_safe_error(self):
        for point in ([True, 0], [181, 0], [0, 91], [0, math.nan], [0, 1, 2], None):
            for a, b in ((point, [0, 0]), ([0, 0], point)):
                with self.subTest(a=a, b=b):
                    with self.assertRaisesRegex(GeometryError, "^Unsupported or invalid geometry\\.$"):
                        haversine(a, b)


if __name__ == "__main__":
    unittest.main()
