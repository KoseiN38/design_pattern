from pathlib import Path
from typing import List, Optional, Tuple

import japanize_matplotlib # noqa: F401
import matplotlib.pyplot as plt

from src.creation.factory.base.graph import Graph
from src.utils.timer import timer


class PieGraph(Graph):
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
        df = self.data[0]
        if len(df.columns) != 1:
            raise ValueError("Pie chart requires a single column of values")

        values = df[df.columns[0]]
        labels = df.index

        self.ax.pie(
            values, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors
        )
        self.ax.set_title(title or "Pie Chart")
        if legend_loc != "none":
            self.ax.legend(loc=legend_loc)

    @timer
    def save(self, filename: Path | str):
        super().save(filename)
