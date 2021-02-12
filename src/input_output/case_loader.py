from typing import List

import pandas as pd

from model.event import Event


class CaseLoader:

    @classmethod
    def load_case(cls, path: str) -> List[Event]:
        case_data = pd.read_csv(path, sep=';')
        return [
            Event.from_dict(row)
            for _, row
            in case_data.iterrows()
        ]
