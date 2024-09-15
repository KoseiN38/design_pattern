from pathlib import Path
from typing import List, Optional, Tuple

import japanize_matplotlib # noqa: F401
import matplotlib.pyplot as plt

from src.creation.factory.base.graph import Graph
from src.utils.timer import timer


class BarGraph(Graph):
    @timer
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
        if style:
            plt.style.use(style)
        bar_width = 0.35
        for i, df in enumerate(self.data):
            color = colors[i] if colors and i < len(colors) else None
            df.plot(kind="bar", ax=self.ax, position=i, width=bar_width, color=color)
        self.ax.set_title(title or "Bar Graph")
        self.ax.set_xlabel(xlabel or "Categories")
        self.ax.set_ylabel(ylabel or "Values")
        if xlim:
            self.ax.set_xlim(xlim)
        if ylim:
            self.ax.set_ylim(ylim)
        self.ax.legend(loc=legend_loc)

    @timer
    def save(self, filename: Path | str):
        super().save(filename)
