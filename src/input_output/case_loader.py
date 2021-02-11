from typing import List

import pandas as pd

from model.event import Event
from model.event_type import EventType


class CaseLoader:

    @staticmethod
    def load_case(path: str) -> List[Event]:
        case_data = pd.read_csv(path, sep=';')
        return [
            Event(
                identifier=int(row["OrderNumber"]),
                x=row["X"],
                y=row["Y"],
                volume=row["Volume"],
                event_type=EventType.parse_from_string(row["Type"])
            )
            for _, row
            in case_data.iterrows()
        ]
