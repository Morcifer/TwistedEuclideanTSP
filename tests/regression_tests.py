from unittest import TestCase

from algorithm.algorithm_route import AlgorithmRoute
from algorithm.route_picker import RoutePicker
from input_output.case_loader import CaseLoader


class RegressionTest(TestCase):
    path = "../data/200_case.csv"

    def test_full_run_capacity_200(self):
        result = self._run_default_case(200)
        self.assertTrue(result.is_route_valid())

    def test_full_run_capacity_400(self):
        result = self._run_default_case(400)
        self.assertTrue(result.is_route_valid())

    def _run_default_case(
            self,
            vehicle_capacity: int
    ) -> AlgorithmRoute:
        events = CaseLoader.load_case(self.path)

        route_picker = RoutePicker(events, vehicle_capacity)
        return route_picker.find_best_route()
