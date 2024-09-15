from abc import ABC, abstractmethod
from typing import List

import pandas as pd

from src.creation.factory.base.graph import Graph


class GraphCreator(ABC):
    @abstractmethod
    def create_graph(self, data: List[pd.DataFrame]) -> Graph:
        pass
