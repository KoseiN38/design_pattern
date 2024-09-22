from abc import ABC, abstractmethod
from typing import Optional

from src.behavior.cor.error.error_handle import HandleError
from src.behavior.cor.models.request import Request
from src.utils.logger import logger


class Handler(ABC):
    def __init__(self, next_handler: Optional["Handler"] = None):
        self._next_handler = next_handler

    def handle(self, request: Request) -> None:
        """チェーン連鎖プロセスを実行する.

        requestオブジェクトを更新しながら、入れ子になっている認証プロセスを順番に実行する.

        Args:
            request (Request): _description_

        Raises:
            e: _description_
        """
        try:
            # ハンドラーを実行する
            self._handle(request)
            # 次のハンドラーを実行する
            if self._next_handler:
                self._next_handler.handle(request)

        except HandleError as e:
            raise e
        except Exception as e:
            logger.error("An Unexpected Error has occurred")
            raise e

    @abstractmethod
    def _handle(self, request: Request) -> None:
        """ハンドラーの具体的処理を記述する.

        Args:
            request (Request): _description_
        """
