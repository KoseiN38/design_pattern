from typing import Literal

from src.utils.logger import logger


class DatabaseConnector:
    _instance = None

    def __new__(cls, name):
        """クラスの唯一のインスタンスを作成・返却する.

        Args:
            name (_type_): 初期化で渡されれるデータベース名称
        """
        # インスタンス未作成ならば、作成する
        if cls._instance is None:
            cls._instance = super(DatabaseConnector, cls).__new__(cls)
            cls._instance.__init__(name)  # __init__の引数にnameを渡す
        return cls._instance

    def __init__(self, name: Literal["postgres", "mysql", "sqlite3"]):
        """初期化.

        初期化済みフラグを設け、2度目以降の呼び出しは処理しない.

        Args:
            name (_type_): データベース名称
        """
        if not hasattr(self, "initialized"):
            self.name = name
            self.initialized = True

    def connect(self):
        logger.info(f"データベース({self.name})に接続しました.")
