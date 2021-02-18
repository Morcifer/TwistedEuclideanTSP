from typing import List

import matplotlib.pyplot as plt

from model.event import Event
from model.event_type import EventType


class SolutionPlotter:

    @classmethod
    def plot_solution(cls, all_events: List[Event], route: List[Event]) -> None:
        plt.plot(
            SolutionPlotter.get_xs(all_events, EventType.DELIVERY),
            SolutionPlotter.get_ys(all_events, EventType.DELIVERY),
            'ok')

        plt.plot(
            SolutionPlotter.get_xs(all_events, EventType.PICKUP),
            SolutionPlotter.get_ys(all_events, EventType.PICKUP),
            'ob')

        plt.plot(
            SolutionPlotter.get_xs(route, EventType.UNKNOWN),
            SolutionPlotter.get_ys(route, EventType.UNKNOWN),
            '-or')

        plt.show()

    @classmethod
    def get_xs(cls, events: List[Event], event_type: EventType) -> List[float]:
        if event_type.name == event_type.UNKNOWN.name:
            return [e.x for e in events]
        return [e.x for e in events if e.event_type.name == event_type.name]

    @classmethod
    def get_ys(cls, events: List[Event], event_type: EventType) -> List[float]:
        if event_type.name == event_type.UNKNOWN.name:
            return [e.y for e in events]
        return [e.y for e in events if e.event_type.name == event_type.name]
