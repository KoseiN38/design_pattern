# 概要

クラスのインスタンスが 1 つだけであることを確認し、そのクラスへのグローバル アクセス ポイントを提供します。

## 使用例

* 入力

```python
 poetry run python src/main.py
```

* 出力

```sh
2024-09-15 15:33:55,616 - MyLogger - INFO - データベース(mysql)に接続しました.
2024-09-15 15:33:55,617 - MyLogger - INFO - データベース(mysql)に接続しました.
2024-09-15 15:33:55,617 - MyLogger - INFO - True
```

## 共有事項
