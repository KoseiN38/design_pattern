from typing import List

import pandas as pd

from src.creation.factory.base.graph import Graph
from src.creation.factory.base.graph_create import GraphCreator
from src.creation.factory.models.bar import BarGraph


class BarGraphCreator(GraphCreator):
    def create_graph(self, data: List[pd.DataFrame]) -> Graph:
        return BarGraph(data)
