from typing import List, Union

from src.structure.composite.base.order_component import OrderComponent
from src.structure.composite.models.product import Product


class Box(OrderComponent):
    """個々の製品や小さな箱が含まれることを想定した箱."""

    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self._price = price
        self.contents: List[OrderComponent] = []

    def add(self, item: Union[Product, "Box"]) -> None:
        if not isinstance(item, OrderComponent):
            raise TypeError("item must be an instance of Product or Box")
        self.contents.append(item)

    @property
    def price(self) -> int:
        """本来の箱の価格と、箱に含まれるすべての製品,箱の金額を合計する."""
        return self._price + sum(item.price for item in self.contents)

    def display(self, indent: str = "") -> None:
        """箱の情報と、箱に含まれるすべての製品,箱の金額を合計する."""
        print(f"{indent}+ {self.name} (箱の価格: {self._price}円)")
        for item in self.contents:
            item.display(indent + "  ")
