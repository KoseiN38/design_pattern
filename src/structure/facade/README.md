# 概要

ファイルシステムの操作と簡単な計算を行うシステムを想定し、それらをfacadeパターンでまとめます。

# 入力パラメータ

プログラムは以下の入力パラメータを受け付けます：

| 引数名 | 物理名 | 型 | 必須 | 説明 |
| --- | --- | --- | --- | --- |
| `file` | `--file` | str | NO  | 操作対象となるファイル名 |
| `content` | `--content` | str | YES | 計算対象となる文章 |

# 使用例

```python
 poetry run python src/structure/facade/client.py
 --file "a.txt"
 --content "hello, world."
```

## 共有事項
