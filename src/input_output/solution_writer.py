from typing import List

import pandas as pd

from model.event import Event


class SolutionWriter:

    @classmethod
    def write_solution(cls, path: str, route: List[Event]) -> None:
        data = pd.DataFrame.from_records([e.to_dict() for e in route])
        data.to_csv(path, sep=';')
