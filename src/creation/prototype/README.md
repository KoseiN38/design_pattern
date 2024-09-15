# 概要

このテンプレート オブジェクトをコピーして作成された、テンプレート オブジェクトを使用して作成されるオブジェクトのタイプを指定します。

この例では、異なるハイパーパラメータを持つ決定木モデルを作成し、それをプロトタイプとして使用して新しいインスタンスを生成します。

## 使用例

* 入力

```python
 poetry run python src/main.py
```

* 出力

```sh
2024-09-09 10:35:55,995 - MyLogger - INFO - define model.
2024-09-09 10:35:55,998 - MyLogger - INFO - Prototype
2024-09-09 10:35:55,998 - MyLogger - INFO - params: DecisionTreeClassifierPT(max_depth=5,min_samples_split=2)
2024-09-09 10:35:55,999 - MyLogger - INFO - predict: [1 0]
2024-09-09 10:35:55,999 - MyLogger - INFO - ================================================================================
2024-09-09 10:35:55,999 - MyLogger - INFO - Model 1
2024-09-09 10:35:55,999 - MyLogger - INFO - params: DecisionTreeClassifierPT(max_depth=9,min_samples_split=99)
2024-09-09 10:35:55,999 - MyLogger - INFO - predict: [1 0]
2024-09-09 10:35:55,999 - MyLogger - INFO - ================================================================================
2024-09-09 10:35:55,999 - MyLogger - INFO - Model 2
2024-09-09 10:35:55,999 - MyLogger - INFO - params: DecisionTreeClassifierPT(max_depth=5,min_samples_split=2)
2024-09-09 10:35:55,999 - MyLogger - INFO - predict: [1 0]
```

## 共有事項
