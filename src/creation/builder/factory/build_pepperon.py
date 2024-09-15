from src.creation.builder.base.build import PizzaBuilder
from src.creation.builder.base.pizza import Pizza


class PepperoniPizzaBuilder(PizzaBuilder):
    """ペバロにピザをビルドするクラス.

    Args:
        PizzaBuilder (_type_): _description_
    """

    def __init__(self):
        self.pizza = Pizza()

    def set_size(self):
        self.pizza.size = 8
        return self

    def add_cheeze(self):
        self.pizza.is_cheeze = False
        return self

    def add_topping(self):
        toppings = ["ペパロニ、チーズ"]
        for topping in toppings:
            self.pizza.toppings.append(topping)
        return self

    def build(self) -> Pizza:
        """完成したピザを返す.

        Returns:
            Pizza: _description_
        """
        return self.pizza
