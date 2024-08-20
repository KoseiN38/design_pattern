from abc import ABC, abstractmethod


class OrderComponent(ABC):
    """注文オブジェクトの抽象基底クラス."""

    @property
    @abstractmethod
    def price(self) -> int:
        pass

    @abstractmethod
    def display(self, indent: str = "") -> None:
        pass
