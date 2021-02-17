from typing import List, Set, Dict, Optional

from algorithm.algorithm_event import AlgorithmEvent


class AlgorithmRoute:
    def __init__(
            self,
            capacity: int,
            events: List[AlgorithmEvent]):
        self.__capacity = capacity
        self.__initial_volume = 0
        self.__remaining_capacity = capacity

        self.events: List[AlgorithmEvent] = list()
        self.event_ids: Set[int] = set()

        for event in events:
            self.add_event(event)

    def get_remaining_capacity(self) -> int:
        return self.__remaining_capacity

    def has_capacity_left(self) -> bool:
        return self.__remaining_capacity > 0

    def does_event_fit(self, event: AlgorithmEvent) -> bool:
        if event.is_delivery():
            return self.__initial_volume + event.volume <= self.__capacity

        if event.is_pickup():
            return self.__remaining_capacity - event.volume >= 0

        return True

    def add_event(
            self,
            event: AlgorithmEvent,
            spot: Optional[int] = None
    ) -> None:
        if spot is None:
            self.events.append(event)
        else:
            self.events.insert(spot, event)

        self.event_ids.add(event.identifier)

        if event.is_delivery():
            self.__initial_volume += event.volume
            self.__remaining_capacity -= event.volume

        if event.is_pickup():
            self.__remaining_capacity += event.volume

    def add_event_in_best_spot(
            self,
            event: AlgorithmEvent,
            distance_dictionary: Dict[int, Dict[int, float]]
            ) -> None:
        best_location = 1
        best_distance = float("inf")

        for location in range(1, len(self.events)):
            event_before = self.events[location-1]
            event_after = self.events[location]
            extra_distance = (
                    distance_dictionary[event_before.identifier][event.identifier]
                    + distance_dictionary[event.identifier][event_after.identifier]
                    - distance_dictionary[event_before.identifier][event_after.identifier]
            )
            if extra_distance < best_distance:
                best_location = location
                best_distance = extra_distance

        self.add_event(event, best_location)

    def is_event_in_route(self, event: AlgorithmEvent) -> bool:
        return event.identifier in self.event_ids

    def copy(self) -> 'AlgorithmRoute':
        result = AlgorithmRoute(
            self.__capacity,
            self.events
        )

        return result
