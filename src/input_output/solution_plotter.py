from typing import List

import matplotlib.pyplot as plt

from model.event import Event


class SolutionPlotter:

    @classmethod
    def plot_solution(cls, all_events: List[Event], route: List[Event]) -> None:
        plt.plot(
            SolutionPlotter.get_xs(all_events),
            SolutionPlotter.get_ys(all_events),
            'ok')

        plt.plot(
            SolutionPlotter.get_xs(route),
            SolutionPlotter.get_ys(route),
            '-or')

        plt.show()

    @classmethod
    def get_xs(cls, events: List[Event]) -> List[float]:
        return [e.x for e in events]

    @classmethod
    def get_ys(cls, events: List[Event]) -> List[float]:
        return [e.y for e in events]
