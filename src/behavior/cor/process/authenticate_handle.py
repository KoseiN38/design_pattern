from src.behavior.cor.base.base_handle import Handler
from src.behavior.cor.error.error_handle import AuthenticationHandleError
from src.behavior.cor.models.request import Request
from src.behavior.cor.params.params import AUTH_PASSWORD, AUTH_USERNAME
from src.utils.logger import logger
from src.utils.timer import timer


class AuthenticationHandler(Handler):
    """ユーザー認証を行う.

    Args:
        Handler (_type_): _description_
    """

    @timer
    def _handle(self, request: Request) -> None:
        # 実際の環境では、データベースやIDプロバイダーとの連携が必要です
        if request.username == AUTH_USERNAME and request.password == AUTH_PASSWORD:
            request.is_authenticated = True
            logger.info("Authentication successful")
        else:
            raise AuthenticationHandleError("Invalid username or password")
