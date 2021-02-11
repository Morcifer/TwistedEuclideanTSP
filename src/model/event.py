from dataclasses import dataclass

from model.event_type import EventType


@dataclass
class Event:
    identifier: int
    x: float
    y: float
    volume: int
    event_type: EventType

    def __init__(self, identifier: int, x: float, y: float, volume: int, event_type: EventType):
        self.identifier = identifier
        self.x = x
        self.y = y
        self.volume = volume
        self.event_type = event_type
