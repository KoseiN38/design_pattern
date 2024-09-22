class HandleError(Exception):
    """認証システムのエラーハンドリングの抽象クラス.

    Args:
        Exception (_type_): _description_
    """


class AuthenticationHandleError(HandleError):
    """ユーザー認証失敗のエラーを検知する.

    Args:
        HandleError (_type_): _description_
    """


class AuthorizationHandleError(HandleError):
    """ユーザー権限のエラーを検知する.

    Args:
        HandleError (_type_): _description_
    """


class ValidationHandleError(HandleError):
    """入力値の検証時のエラーを検知する.

    Args:
        HandleError (_type_): _description_
    """


class CachingHandleError(HandleError):
    """認証情報キャッシュ時のエラーを検知する.

    Args:
        HandleError (_type_): _description_
    """
