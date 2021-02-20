from typing import List, Set, Dict, Optional

from algorithm.algorithm_event import AlgorithmEvent


class AlgorithmRoute:
    def __init__(
            self,
            capacity: int,
            events: List[AlgorithmEvent]
    ):
        self.__capacity = capacity
        self.__initial_used_capacity = 0
        self.__remaining_capacity = capacity

        self.__event_ids: Set[int] = set()

        self.events: List[AlgorithmEvent] = list()

        for event in events:
            self.add_event(event)

    def get_remaining_capacity(self) -> int:
        return self.__remaining_capacity

    def has_capacity_left(self) -> bool:
        return self.__remaining_capacity > 0

    def does_event_fit(
            self,
            event: AlgorithmEvent,
            spot: Optional[int] = None
    ) -> bool:
        if event.is_delivery():
            return self.__initial_used_capacity + event.volume <= self.__capacity

        if event.is_pickup():
            # At the end of the route, like add_event
            if spot is None:
                return self.__capacity >= event.volume
            else:
                # TODO: Bad performance. Store capacity per spot.
                remaining_volume_to_delivery = sum(map(lambda x: x.volume, self.events[spot:]))
                return self.__capacity - remaining_volume_to_delivery >= event.volume

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

        self.__event_ids.add(event.identifier)

        if event.is_delivery():
            self.__initial_used_capacity += event.volume
            self.__remaining_capacity -= event.volume

        if event.is_pickup():
            self.__remaining_capacity += event.volume

    # TODO: Add tests for this method.
    def find_best_event_spot_and_distance(
            self,
            event: AlgorithmEvent,
            distance_dictionary: Dict[int, Dict[int, float]]
    ) -> (int, float):
        best_spot = 1
        best_distance = float("inf")

        for spot in range(1, len(self.events)):
            event_before = self.events[spot-1]
            event_after = self.events[spot]
            extra_distance = (
                    distance_dictionary[event_before.identifier][event.identifier]
                    + distance_dictionary[event.identifier][event_after.identifier]
                    - distance_dictionary[event_before.identifier][event_after.identifier]
            )

            if extra_distance < best_distance:
                # For pickups, we have to also make sure it fits in the spot
                if (not event.is_pickup()) or self.does_event_fit(event, spot):
                    best_spot = spot
                    best_distance = extra_distance

        return best_spot, best_distance

    def add_event_in_best_spot(
            self,
            event: AlgorithmEvent,
            distance_dictionary: Dict[int, Dict[int, float]]
    ) -> None:
        best_spot, _ = self.find_best_event_spot_and_distance(event, distance_dictionary)

        self.add_event(event, best_spot)

    def two_opt(
            self,
            distance_dictionary: Dict[int, Dict[int, float]]
    ) -> None:
        improvement_found = True

        while improvement_found:
            improvement_found = False

            for i in range(1, len(self.events) - 2):
                i_dist_pre_swap = distance_dictionary[self.events[i-1].identifier][self.events[i].identifier]

                for j in range(i+1, len(self.events) - 1):
                    j_dist_pre_swap = distance_dictionary[self.events[j].identifier][self.events[j+1].identifier]
                    d1 = i_dist_pre_swap + j_dist_pre_swap

                    i_dist_post_swap = distance_dictionary[self.events[i-1].identifier][self.events[j].identifier]
                    j_dist_post_swap = distance_dictionary[self.events[i].identifier][self.events[j+1].identifier]

                    d2 = i_dist_post_swap + j_dist_post_swap

                    if d1 > d2:
                        self.events[i], self.events[j] = self.events[j], self.events[i]
                        improvement_found = True

                    if improvement_found:
                        break  # Out of j loop

                if improvement_found:
                    break  # Out of i loop

    def is_event_in_route(self, event: AlgorithmEvent) -> bool:
        return event.identifier in self.__event_ids

    def is_route_valid(self) -> bool:
        pickups = [e for e in self.events if e.is_pickup()]

        if len(pickups) != 1:
            return False

        current_used_capacity = sum([e.volume for e in self.events if e.is_delivery()])

        for event in self.events:
            if event.is_pickup():
                current_used_capacity += event.volume
            else:
                current_used_capacity -= event.volume

            if current_used_capacity > self.__capacity:
                return False

        return True

    def get_total_distance(self) -> float:
        result = 0
        for i in range(0, len(self.events) - 1):
            result += self.events[i].get_distance(self.events[i+1])
        return result

    def copy(self) -> 'AlgorithmRoute':
        result = AlgorithmRoute(
            self.__capacity,
            self.events
        )

        return result
