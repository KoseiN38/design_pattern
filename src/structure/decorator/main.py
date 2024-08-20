import time

from src.utils.logger import logger
from src.utils.timer import timer
from src.utils.trace import trace


# NOTE: decoratorは下から上に向かって実行される（例: main→trace→timer）
@timer
@trace
def main(message) -> str:
    """デコレーターを使った呼び出しを行う関数."""
    try:
        time.sleep(5)
        logger.info(message)
        return "finish"
    except Exception as e:
        logger.error(e)
        raise e


if __name__ == "__main__":
    message = "hello world."
    main(message)
