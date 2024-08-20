"""デコレーターとして使用する.

ex>
@timer
def my_func():
    pass
"""

import time
from functools import wraps


def timer(func):
    """処理時間を計測するデコレーター."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__}の実行時間: {end_time - start_time:.4f}秒")
        return result

    return wrapper
