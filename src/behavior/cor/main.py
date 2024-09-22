from src.behavior.cor.base.base_handle import Handler
from src.behavior.cor.models.request import Request
from src.behavior.cor.process.authenticate_handle import AuthenticationHandler
from src.behavior.cor.process.authorizate_handle import AuthorizationHandler
from src.behavior.cor.process.cache_handle import CachingHandler
from src.behavior.cor.process.validate_handle import ValidationHandler
from src.utils.logger import logger


def setup_chain() -> Handler:
    """処理の順番に従って連鎖してハンドラーをインスタンス化する.

    Chain Of Responsibilityの肝となる処理.

    Returns:
        Handler: _description_
    """
    caching = CachingHandler()
    validation = ValidationHandler(caching)
    authorization = AuthorizationHandler(validation)
    authentication = AuthenticationHandler(authorization)
    return authentication


def process_login(username: str, password: str) -> bool:
    """認証プロセスを実行する.

    最後のキャッシュ処理完了のRequest情報を返す

    Args:
        username (str): _description_
        password (str): _description_

    Returns:
        bool: _description_
    """
    try:
        request = Request(username, password)
        chain = setup_chain()
        chain.handle(request)
    except Exception as e:
        logger.error(e)
    finally:
        return request.__dict__


if __name__ == "__main__":
    logger.info(
        "start the authentication process",
    )
    result = process_login(
        username="admin",
        password="password",
    )
    logger.info(result)
