import math

from model.event import Event
from model.event_type import EventType


class AlgorithmEvent(Event):
    def __init__(
            self,
            identifier: int,
            x: float,
            y: float,
            volume: int,
            event_type: EventType):
        super().__init__(identifier, x, y, volume, event_type)

    def is_delivery(self):
        return self.event_type.name == EventType.DELIVERY.name

    def is_pickup(self):
        return self.event_type.name == EventType.PICKUP.name

    def get_distance(self, algorithm_event: 'AlgorithmEvent') -> float:
        dx_2 = math.pow(self.x - algorithm_event.x, 2)
        dy_2 = math.pow(self.y - algorithm_event.y, 2)
        return math.sqrt(dx_2 + dy_2)
