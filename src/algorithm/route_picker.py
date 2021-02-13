from typing import List, Dict

from algorithm.algorithm_event import AlgorithmEvent
from algorithm.algorithm_route import AlgorithmRoute
from model.event import Event
from model.event_type import EventType


class RoutePicker:
    def __init__(self, events: List[Event], capacity: int):
        self.__depot_identifier = -1
        self.__origin = AlgorithmEvent(self.__depot_identifier, 0, 0, 0, EventType.ORIGIN)
        self.__destination = AlgorithmEvent(self.__depot_identifier, 0, 0, 0, EventType.DESTINATION)

        self.__algorithm_events = [AlgorithmEvent(**event.__dict__) for event in events]

        self.__pickups = [
            event
            for event
            in self.__algorithm_events
            if event.is_pickup()]

        self.__deliveries = [
            event
            for event
            in self.__algorithm_events
            if event.is_delivery()]

        self.__capacity = capacity

        self.__distances_dictionary = self._calculate_distance_dict(self.__algorithm_events)

    def find_best_route(self) -> AlgorithmRoute:
        route = AlgorithmRoute(self.__capacity)

        # Start at a depot
        route.add_event(self.__origin)

        # Add deliveries until space is gone
        for delivery in self.__deliveries:
            if route.does_event_fit(delivery):
                route.add_event(delivery)

        # Add the best pickup
        if len(self.__pickups) > 0:
            route.add_event(self.__pickups[0])

        # End at a depot
        route.add_event(self.__destination)

        return route

    def _calculate_distance_dict(
            self,
            events: List[AlgorithmEvent]
    ) -> Dict[int, Dict[int, float]]:
        result = {
            event.identifier: dict()
            for event
            in events
        }
        result[self.__depot_identifier] = dict()

        for event1 in events:
            distance = self.__origin.get_distance(event1)

            result[self.__depot_identifier][event1.identifier] = distance
            result[event1.identifier][self.__depot_identifier] = distance

            for event2 in events:
                distance = event1.get_distance(event2)
                result[event1.identifier][event2.identifier] = distance
                result[event2.identifier][event1.identifier] = distance

        return result
