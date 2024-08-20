# 概要

デコレーターパターン（Decorator Pattern）は、オブジェクトに対して動的に機能を追加するためのデザインパターンです。Pythonでは、関数デコレータを使ってこのパターンを簡単に実装できます。

例えば処理時間を計測したり、実行ログを出力するデコレーターを実装する。

## 使用例

* 入力

```python
 poetry run python src/main.py
```

* 出力

```sh
INFO:root:mainが呼び出されました。引数: ('hello world.',), キーワード引数: {}
2024-08-20 22:19:32,788 - MyLogger - INFO - hello world.
INFO:MyLogger:hello world.
INFO:root:mainが終了しました。戻り値: finish
mainの実行時間: 5.0065秒
```

## 共有事項
