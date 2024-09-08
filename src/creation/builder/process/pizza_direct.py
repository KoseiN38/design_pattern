from src.creation.builder.base.build import PizzaBuilder


class PizzaDirector:
    """ピザ作成プロセスを制御する."""

    def __init__(self, builder: PizzaBuilder):
        """オブジェクトを初期化する.

        Args:
            builder (PizzaBuilder): 使用するビルダーオブジェクト
        """
        self.builder = builder

    def make_pizza(self):
        """指定されたピザを作成する.

        Returns:
            _type_: _description_
        """
        return self.builder.set_size().add_cheeze().add_topping().build()
