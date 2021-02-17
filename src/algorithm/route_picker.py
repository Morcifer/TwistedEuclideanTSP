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
        empty_route = AlgorithmRoute(
            self.__capacity,
            [self.__origin, self.__destination])

        greedy_initial_route = self._construct_greedy_delivery_route(empty_route)
        route_with_pickup = self._add_pickup_to_route(greedy_initial_route)

        return route_with_pickup

    def _construct_greedy_delivery_route(
            self,
            input_route: AlgorithmRoute
    ) -> AlgorithmRoute:
        result = input_route.copy()

        # We want to visit as many deliveries as possible, and then shorten distance
        # so we sort by smallest to biggest and then closest (to depot, not in general)
        deliveries_to_investigate = sorted(
            self.__deliveries,
            key=lambda x: (
                x.volume,
                self.__distances_dictionary[self.__depot_identifier][x.identifier]))

        # While there is capacity remaining and deliveries remaining:
        while result.has_capacity_left() and len(deliveries_to_investigate) > 0:
            # Find max volume that fits
            remaining_capacity = result.get_remaining_capacity()
            max_volume = 0

            for delivery in deliveries_to_investigate:
                if delivery.volume <= remaining_capacity:
                    max_volume = delivery.volume
                    remaining_capacity -= delivery.volume

            # Limit deliveries into ones that are under volume
            deliveries_to_investigate = [
                delivery
                for delivery
                in deliveries_to_investigate
                if delivery.volume <= max_volume and (not result.is_event_in_route(delivery))
            ]

            # Find best delivery based on last location visited
            # TODO: Find best delivery based on existing pickups in route
            # TODO: Get rid of the hard-coded -2 for the event before the destination
            closest_delivery = min(
                deliveries_to_investigate,
                key=lambda x: self.__distances_dictionary[result.events[-2].identifier][x.identifier])

            # Add that best pickup in the best location
            result.add_event_in_best_spot(closest_delivery, self.__distances_dictionary)

        return result

    def _add_pickup_to_route(
            self,
            input_route: AlgorithmRoute
    ) -> AlgorithmRoute:
        result = input_route.copy()

        # TODO: Make sure that the chosen pickup fits in the right place
        #  (including possibly reversing the route)
        if len(self.__pickups) > 0:
            result.add_event_in_best_spot(
                self.__pickups[0],
                self.__distances_dictionary)

        return result


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
        result[self.__depot_identifier][self.__depot_identifier] = 0

        for event1 in events:
            distance = self.__origin.get_distance(event1)

            result[self.__depot_identifier][event1.identifier] = distance
            result[event1.identifier][self.__depot_identifier] = distance

            for event2 in events:
                distance = event1.get_distance(event2)
                result[event1.identifier][event2.identifier] = distance
                result[event2.identifier][event1.identifier] = distance

        return result
