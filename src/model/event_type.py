from enum import Enum


class EventType(Enum):
    UNKNOWN = 0
    PICKUP = 1
    DELIVERY = 2

    def is_valid(self) -> bool:
        return self == EventType.PICKUP or self == EventType.DELIVERY

    @staticmethod
    def parse_from_string(string: str) -> 'EventType':
        if string == "P":
            return EventType.PICKUP

        if string == "D":
            return EventType.DELIVERY

        return EventType.UNKNOWN
