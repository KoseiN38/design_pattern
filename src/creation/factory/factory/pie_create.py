from typing import List

import pandas as pd

from src.creation.factory.base.graph import Graph
from src.creation.factory.base.graph_create import GraphCreator
from src.creation.factory.models.pie import PieGraph


class PieGraphCreator(GraphCreator):
    def create_graph(self, data: List[pd.DataFrame]) -> Graph:
        return PieGraph(data)
