from src.creation.builder.base.build import PizzaBuilder
from src.creation.builder.base.pizza import Pizza


class MargheritaPizzaBuilder(PizzaBuilder):
    """マルゲリータピザをビルドするクラス.

    Args:
        PizzaBuilder (_type_): _description_
    """

    def __init__(self):
        self.pizza = Pizza()

    def set_size(self):
        self.pizza.size = 10
        return self

    def add_cheeze(self):
        self.pizza.is_cheeze = True
        return self

    def add_topping(self):
        for topping in ["バジル", "モッツァレラチーズ"]:
            self.pizza.toppings.append(topping)
        return self

    def build(self) -> Pizza:
        """完成したピザを返す.

        Returns:
            Pizza: _description_
        """
        return self.pizza
