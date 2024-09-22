from src.behavior.cor.base.base_handle import Handler
from src.behavior.cor.error.error_handle import ValidationHandleError
from src.behavior.cor.models.request import Request
from src.behavior.cor.params.params import ALLOW_LENGTH_PASSWORD, ALLOW_LENGTH_USERNAME
from src.utils.logger import logger
from src.utils.timer import timer


class ValidationHandler(Handler):
    """入力値の検証を行う.

    Args:
        Handler (_type_): _description_
    """

    @timer
    def _handle(self, request: Request) -> None:
        # 実際の環境では、入力値の検証やセキュリティチェックを行います
        if (
            request.is_authorized
            and len(request.username) > ALLOW_LENGTH_USERNAME
            and len(request.password) > ALLOW_LENGTH_PASSWORD
        ):
            request.is_validated = True
            logger.info("Validation successful")
        else:
            raise ValidationHandleError("Validation failed")
