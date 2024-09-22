from src.behavior.cor.base.base_handle import Handler
from src.behavior.cor.error.error_handle import CachingHandleError
from src.behavior.cor.models.request import Request
from src.utils.logger import logger
from src.utils.timer import timer


class CachingHandler(Handler):
    """認証情報のキャッシュを行う.

    Args:
        Handler (_type_): _description_
    """

    @timer
    def _handle(self, request: Request) -> None:
        # 実際の環境では、キャッシュの保存と取得を行います
        if request.is_validated:
            request.is_cached = True
            logger.info("Caching successful")
        else:
            raise CachingHandleError("Cannot cache invalid request")
