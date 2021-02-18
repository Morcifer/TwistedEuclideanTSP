from unittest import TestCase

from src.algorithm.algorithm_event import AlgorithmEvent
from src.algorithm.algorithm_route import AlgorithmRoute
from src.model.event_type import EventType


class AlgorithmRouteTest(TestCase):
    def test_route_add_event_fits_one_delivery(self):
        route = AlgorithmRoute(100, list())
        delivery = self._create_dummy_event(100, EventType.DELIVERY)

        self.assertTrue(route.does_event_fit(delivery))

        route.add_event(delivery)

        self.assertFalse(route.has_capacity_left())
        self.assertEqual(1, len(route.events))

    def test_route_add_event_multiple_deliveries(self):
        route = AlgorithmRoute(100, list())
        delivery1 = self._create_dummy_event(60, EventType.DELIVERY)
        delivery2 = self._create_dummy_event(40, EventType.DELIVERY)
        delivery3 = self._create_dummy_event(60, EventType.DELIVERY)

        self.assertTrue(route.does_event_fit(delivery1))

        route.add_event(delivery1)

        self.assertTrue(route.has_capacity_left())
        self.assertTrue(route.does_event_fit(delivery2))
        self.assertFalse(route.does_event_fit(delivery3))

        route.add_event(delivery2)

        self.assertEqual(2, len(route.events))

    def test_route_add_event_pickup(self):
        route = AlgorithmRoute(100, list())
        delivery = self._create_dummy_event(60, EventType.DELIVERY)
        pickup = self._create_dummy_event(60, EventType.PICKUP)

        self.assertTrue(route.does_event_fit(pickup))

        route.add_event(delivery)

        self.assertTrue(route.does_event_fit(pickup))
        self.assertFalse(route.does_event_fit(pickup, 0))
        self.assertTrue(route.does_event_fit(pickup, 1))

    def _create_dummy_event(self, volume: int, event_type: EventType) -> AlgorithmEvent:
        return AlgorithmEvent(0, 0, 0, volume, event_type)
