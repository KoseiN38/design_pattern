from typing import List, Optional, Tuple

import pandas as pd

from src.creation.factory.base.graph_create import GraphCreator
from src.utils.logger import logger


def create_and_save_graph(
    creator: GraphCreator,
    data: List[pd.DataFrame],
    filename: str,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    colors: Optional[List[str]] = None,
    style: Optional[str] = None,
    xlim: Optional[Tuple[float, float]] = None,
    ylim: Optional[Tuple[float, float]] = None,
    legend_loc: str = "best",
):
    """factory methodパターンに従って、異なる種類のグラフを作成するファクトリーを呼び出す.

    Args:
        creator (GraphCreator): _description_
        data (List[pd.DataFrame]): _description_
        filename (str): _description_
        title (Optional[str], optional): _description_. Defaults to None.
        xlabel (Optional[str], optional): _description_. Defaults to None.
        ylabel (Optional[str], optional): _description_. Defaults to None.
        colors (Optional[List[str]], optional): _description_. Defaults to None.
        style (Optional[str], optional): _description_. Defaults to None.
        xlim (Optional[Tuple[float, float]], optional): _description_. Defaults to None.
        ylim (Optional[Tuple[float, float]], optional): _description_. Defaults to None.
        legend_loc (str, optional): _description_. Defaults to 'best'.
    """
    graph = creator.create_graph(data)
    graph.plot(
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        colors=colors,
        style=style,
        xlim=xlim,
        ylim=ylim,
        legend_loc=legend_loc,
    )
    graph.save(filename)
    logger.info(f"Graph saved as {filename}")
