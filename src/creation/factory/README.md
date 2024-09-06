# 概要

オブジェクトクラスのインターフェースを定義して、具体的なクラスのインスタンスをどのクラスにするかはサブクラスで定義する.

この例では、異なる種類のグラフ（折線グラフ、棒グラフ、円グラフ）を作成するファクトリーを実装します。

## ダイアグラム図

```mermaid
classDiagram
    class Graph {
        <<abstract>>
        +data: List[pd.DataFrame]
        +fig: matplotlib.figure.Figure
        +ax: matplotlib.axes.Axes
        +plot(title, xlabel, ylabel, colors, style, xlim, ylim, legend_loc)*
        +save(filename)
    }
    class LineGraph {
        +plot(title, xlabel, ylabel, colors, style, xlim, ylim, legend_loc)
    }
    class BarGraph {
        +plot(title, xlabel, ylabel, colors, style, xlim, ylim, legend_loc)
    }
    class PieGraph {
        +plot(title, xlabel, ylabel, colors, style, xlim, ylim, legend_loc)
    }
    class GraphCreator {
        <<abstract>>
        +create_graph(data: List[pd.DataFrame])*: Graph
    }
    class LineGraphCreator {
        +create_graph(data: List[pd.DataFrame]): LineGraph
    }
    class BarGraphCreator {
        +create_graph(data: List[pd.DataFrame]): BarGraph
    }
    class PieGraphCreator {
        +create_graph(data: List[pd.DataFrame]): PieGraph
    }

    Graph <|-- LineGraph
    Graph <|-- BarGraph
    Graph <|-- PieGraph
    GraphCreator <|-- LineGraphCreator
    GraphCreator <|-- BarGraphCreator
    GraphCreator <|-- PieGraphCreator
    GraphCreator ..> Graph : creates
    LineGraphCreator ..> LineGraph : creates
    BarGraphCreator ..> BarGraph : creates
    PieGraphCreator ..> PieGraph : creates

```

## 使用例

* 入力

```python
 poetry run python src/main.py
```

* 出力

```sh
plotの実行時間: 0.0243秒
saveの実行時間: 0.1323秒
2024-09-06 10:54:44,397 - MyLogger - INFO - Graph saved as data/advanced_line_graph.png
plotの実行時間: 0.0138秒
saveの実行時間: 0.1341秒
2024-09-06 10:54:44,563 - MyLogger - INFO - Graph saved as data/advanced_bar_graph.png
plotの実行時間: 0.0107秒
saveの実行時間: 0.1235秒
2024-09-06 10:54:44,716 - MyLogger - INFO - Graph saved as data/advanced_pie_chart.png
```

## 共有事項
