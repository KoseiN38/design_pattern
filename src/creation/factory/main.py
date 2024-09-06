from pathlib import Path

import pandas as pd

from src.creation.factory.factory.bar_create import BarGraphCreator
from src.creation.factory.factory.line_create import LineGraphCreator
from src.creation.factory.factory.pie_create import PieGraphCreator
from src.creation.factory.process.create_graph import create_and_save_graph

if __name__ == "__main__":
    # Sample data
    data1 = pd.DataFrame(
        {
            "Category": ["りんご", "バナナ", "ブドウ", "オレンジ"],
            "Value1": [25, 40, 30, 55],
        }
    ).set_index("Category")

    data2 = pd.DataFrame(
        {
            "Category": ["りんご", "バナナ", "ブドウ", "オレンジ"],
            "Value2": [30, 35, 25, 60],
        }
    ).set_index("Category")

    output_dir = Path("data")

    # Create and save different types of graphs with custom settings
    create_and_save_graph(
        LineGraphCreator(),
        [data1, data2],
        output_dir.joinpath("advanced_line_graph.png"),
        title="Monthly Sales Comparison",
        xlabel="Month",
        ylabel="Sales ($)",
        colors=["blue", "red"],
        style="ggplot",
        xlim=(0, 3),
        ylim=(0, 70),
        legend_loc="upper left",
    )

    create_and_save_graph(
        BarGraphCreator(),
        [data1, data2],
        output_dir.joinpath("advanced_bar_graph.png"),
        title="Quarterly Revenue Comparison",
        xlabel="Quarter",
        ylabel="Revenue ($)",
        colors=["green", "orange"],
        style="ggplot",
        ylim=(0, 80),
        legend_loc="upper right",
    )

    create_and_save_graph(
        PieGraphCreator(),
        [data1],
        output_dir.joinpath("advanced_pie_chart.png"),
        title="Market Share by Product",
        colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"],
        style="classic",
        legend_loc="center left",
    )
