# 概要

デザインパターンの概要を記載します

デザインパターンを駆使した実装例の説明をします


## 入力パラメータ

プログラムは以下の入力パラメータを受け付けます：

| 引数名 | 物理名 | 型 | 必須 | 説明 |
| --- | --- | --- | --- | --- |
| `params` | `--params` | str | YES  | 入力パラメータ |

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
 poetry run python src/sample.py
 --text "hello, world."
```

* 出力

```sh
```

## 共有事項
