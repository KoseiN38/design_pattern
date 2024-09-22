from src.behavior.cor.base.base_handle import Handler
from src.behavior.cor.error.error_handle import AuthorizationHandleError
from src.behavior.cor.models.request import Request
from src.utils.logger import logger
from src.utils.timer import timer


class AuthorizationHandler(Handler):
    """ユーザー権限を取得する.

    Args:
        Handler (_type_): _description_
    """

    @timer
    def _handle(self, request: Request) -> None:
        # 実際の環境では、ユーザーの権限をチェックします
        if request.is_authenticated:
            request.is_authorized = True
            logger.info("Authorization successful")
        else:
            raise AuthorizationHandleError("User is not authenticated")
