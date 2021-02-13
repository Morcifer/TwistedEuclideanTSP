from typing import List

from algorithm.algorithm_event import AlgorithmEvent


class AlgorithmRoute:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__initial_volume = 0
        self.__remaining_capacity = capacity

        self.events: List[AlgorithmEvent] = list()

    def has_capacity_left(self) -> bool:
        return self.__remaining_capacity > 0

    def does_event_fit(self, event: AlgorithmEvent) -> bool:
        if event.is_delivery():
            return self.__initial_volume + event.volume <= self.__capacity

        if event.is_pickup():
            return self.__remaining_capacity - event.volume >= 0

        return True

    def add_event(self, event: AlgorithmEvent) -> None:
        self.events.append(event)

        if event.is_delivery():
            self.__initial_volume += event.volume
            self.__remaining_capacity -= event.volume

        if event.is_pickup():
            self.__remaining_capacity += event.volume
