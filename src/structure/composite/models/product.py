from src.structure.composite.base.order_component import OrderComponent


class Product(OrderComponent):
    """個々の製品."""

    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self._price = price

    @property
    def price(self) -> int:
        return self._price

    def display(self, indent: str = "") -> None:
        print(f"{indent}- {self.name}: {self.price}円")
