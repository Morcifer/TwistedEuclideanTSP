from unittest import TestCase

from algorithm.algorithm_route import AlgorithmRoute
from algorithm.route_picker import RoutePicker
from input_output.case_loader import CaseLoader


class RegressionTest(TestCase):
    path = "../data/200_case.csv"

    # Lower-bound test (single delivery)
    def test_full_run_capacity_10(self):
        result = self._run_default_case(10)
        self.assertTrue(result.is_route_valid())
        total_distance = result.get_total_distance()
        self.assertAlmostEqual(56, total_distance, places=0)

    def test_full_run_capacity_200(self):
        result = self._run_default_case(200)
        self.assertTrue(result.is_route_valid())
        total_distance = result.get_total_distance()
        self.assertAlmostEqual(429, total_distance, places=0)

    def test_full_run_capacity_400(self):
        result = self._run_default_case(400)
        self.assertTrue(result.is_route_valid())
        total_distance = result.get_total_distance()
        self.assertAlmostEqual(774, total_distance, places=0)

    # Upper-bound test (all 102 deliveries fit)
    def test_full_run_capacity_1M(self):
        result = self._run_default_case(1000000)
        self.assertTrue(result.is_route_valid())
        total_distance = result.get_total_distance()
        self.assertEqual(102 + 2 + 1, len(result.events))
        self.assertAlmostEqual(1006, total_distance, places=0)

    def _run_default_case(
            self,
            vehicle_capacity: int
    ) -> AlgorithmRoute:
        events = CaseLoader.load_case(self.path)

        route_picker = RoutePicker(events, vehicle_capacity)
        return route_picker.find_best_route()
