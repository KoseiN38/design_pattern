from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Optional, Tuple

import matplotlib.pyplot as plt
import pandas as pd


# Abstract Product
class Graph(ABC):
    def __init__(self, data: List[pd.DataFrame]):
        """初期化.

        Args:
            data (List[pd.DataFrame]): _description_
        """
        self.data = data
        self.fig, self.ax = plt.subplots(figsize=(12, 7))

    @abstractmethod
    def plot(
        self,
        title: Optional[str] = None,
        xlabel: Optional[str] = None,
        ylabel: Optional[str] = None,
        colors: Optional[List[str]] = None,
        style: Optional[str] = None,
        xlim: Optional[Tuple[float, float]] = None,
        ylim: Optional[Tuple[float, float]] = None,
        legend_loc: str = "best",
    ):
        """グラフを作成する.

        Args:
            title (Optional[str], optional): _description_. Defaults to None.
            xlabel (Optional[str], optional): _description_. Defaults to None.
            ylabel (Optional[str], optional): _description_. Defaults to None.
            colors (Optional[List[str]], optional): _description_. Defaults to None.
            style (Optional[str], optional): _description_. Defaults to None.
            xlim (Optional[Tuple[float, float]], optional): _description_. Defaults to None.
            ylim (Optional[Tuple[float, float]], optional): _description_. Defaults to None.
            legend_loc (str, optional): _description_. Defaults to 'best'.
        """

    @abstractmethod
    def save(self, filename: Path | str):
        """グラフを保存する.

        Args:
            filename (_type_): _description_
        """
        self.fig.tight_layout()
        self.fig.savefig(filename)
        plt.close(self.fig)
