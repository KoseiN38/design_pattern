from abc import ABC, abstractmethod


class PizzaBuilder(ABC):
    """ピザビルダーの抽象基底クラス.

    Args:
        ABC (_type_): _description_
    """

    @abstractmethod
    def set_size(self, size: int):
        """ピザのサイズを定義する.

        Args:
            size (int): サイズ
        """

    @abstractmethod
    def add_cheeze(self, is_cheeeze: bool):
        """ピザのチーズ有無を定義する.

        Args:
            is_cheeeze (bool): チーズの有無
        """

    @abstractmethod
    def add_topping(self, toppings: list):
        """ピザのトッピングを定義する.

        Args:
            toppings (list): トッピングリスト
        """
