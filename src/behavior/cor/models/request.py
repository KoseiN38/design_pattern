class Request:
    """認証情報を管理する."""

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.is_authenticated = False
        self.is_authorized = False
        self.is_validated = False
        self.is_cached = False
