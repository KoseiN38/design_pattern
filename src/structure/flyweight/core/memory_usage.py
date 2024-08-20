import sys
from functools import update_wrapper


def add_memory_usage(cls):
    class Wrapper(cls):
        def get_memory_usage(self):
            total = sys.getsizeof(self)
            for var, value in self.__dict__.items():
                if isinstance(value, (int, str, float, bool)):
                    total += sys.getsizeof(value)
                elif isinstance(value, list):
                    total += sum(
                        (
                            item.get_memory_usage()
                            if hasattr(item, "get_memory_usage")
                            else sys.getsizeof(item)
                        )
                        for item in value
                    )
                elif hasattr(value, "get_memory_usage"):
                    total += value.get_memory_usage()
                else:
                    total += sys.getsizeof(value)
            return total

    # メタデータを手動でコピー
    Wrapper.__name__ = cls.__name__
    Wrapper.__qualname__ = cls.__qualname__
    Wrapper.__module__ = cls.__module__
    Wrapper.__doc__ = cls.__doc__

    # その他の属性をコピー
    update_wrapper(Wrapper, cls, updated=())

    return Wrapper
