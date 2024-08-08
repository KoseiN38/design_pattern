"""デコレーターとして使う.

ex>
@trace
def my_func():
    pass
"""

import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)


def trace(func):
    """実行ログを出力するデコレーター."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(
            f"{func.__name__}が呼び出されました。引数: {args}, キーワード引数: {kwargs}"
        )
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__}が終了しました。戻り値: {result}")
        return result

    return wrapper
