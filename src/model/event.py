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

    def to_dict(self):
        return {
            "OrderNumber": self.identifier,
            "X": self.x,
            "Y": self.y,
            "Volume": self.volume,
            "Type": self.event_type.parse_to_string()
        }

    @staticmethod
    def from_dict(dictionary: dict) -> 'Event':
        return Event(
            identifier=int(dictionary["OrderNumber"]),
            x=dictionary["X"],
            y=dictionary["Y"],
            volume=dictionary["Volume"],
            event_type=EventType.parse_from_string(dictionary["Type"])
        )
