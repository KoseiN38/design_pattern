class FileNotFoundError(Exception):
    """ファイルが存在しなかった場合のエラーハンドリング.

    Args:
        Exception (_type_): _description_
    """


class DocumentNotFoundError(Exception):
    """実行プロセスにドキュメントモデルが存在しなかった場合のエラーハンドリング.

    Args:
        Exception (_type_): _description_
    """


class RequestParameterError(Exception):
    """リクエストパラメーターが期待する形式でなかった場合のエラーハンドリング.

    Args:
        Exception (_type_): _description_
    """
