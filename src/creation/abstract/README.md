# 概要

抽象基底クラスの共通インターフェースを定義して動作することを促進する


この例では、文書処理システムを簡略化して実装します。新しい種類のドキュメント（例：ExcelDocument）を追加する際に、既存のコードを変更することなく、システムを拡張できます。
このコードを実行すると、各ドキュメントの開く、保存、編集操作がコンソールに出力されます。実際のファイル操作は行われませんが、Abstract Methodパターンの使用方法を示すことができます。

## 入力パラメータ

プログラムは以下の入力パラメータを受け付けます：

| 引数名 | 物理名 | 型 | 必須 | 説明 |
| --- | --- | --- | --- | --- |
| `file` | `--file` | str  | YES  | 解析するファイル名のリスト※ |

※ 本レポジトリのルートディレクトリにある`data/`内に対象のファイルが格納されていること。拡張子は`[".txt", ".csv"]`に限定する。

## ダイアグラム図

```mermaid
classDiagram
    class Document {
        <<abstract>>
        +filename: str
        +content: Any
        +__init__(filename: str)
        +open()*
        +save()*
        +edit(new_content: Any)
    }

    class TextDocument {
        +open()
        +save()
    }

    class CSVDocument {
        +open()
        +save(encoding: str, index: bool)
    }

    class DocumentManager {
        -documents: dict
        +add_document(document: Document)
        +remove_document(filename: str)
        +open_all()
        +save_all()
    }

    Document <|-- TextDocument
    Document <|-- CSVDocument
    DocumentManager o-- Document

    note for Document "Abstract base class"
    note for TextDocument "Handles .txt files"
    note for CSVDocument "Handles .csv files using pandas"
    note for DocumentManager "Manages multiple documents"

```

## 使用例

* 入力

```python
 poetry run python src/creation/abstract/main.py
 --file '["test.csv", "test.txt"]'
```

* 出力

```sh
INFO:root:mainが呼び出されました。引数: (['product.csv', 'test_file.txt'],), キーワード引数: {}
2024-08-24 11:52:55,460 - MyLogger - INFO - Opened CSV file: data/product.csv
INFO:MyLogger:Opened CSV file: data/product.csv
2024-08-24 11:52:55,460 - MyLogger - INFO -    id    item  price
0   0   apple    100
1   1  banana    200
2   2  orange    110
3   3    gine    140
INFO:MyLogger:   id    item  price
0   0   apple    100
1   1  banana    200
2   2  orange    110
3   3    gine    140
2024-08-24 11:52:55,466 - MyLogger - INFO - Opened text file: data/test_file.txt
INFO:MyLogger:Opened text file: data/test_file.txt
2024-08-24 11:52:55,467 - MyLogger - INFO - "hello world."
INFO:MyLogger:"hello world."
INFO:root:mainが終了しました。戻り値: None
mainの実行時間: 0.0087秒
```

## 共有事項
