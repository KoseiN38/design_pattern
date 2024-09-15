class Pizza:
    """ピザ生地を作成する基底クラス."""

    def __init__(self):
        """初期化する."""
        self.size = None
        self.is_cheeze = False
        self.toppings = []

    def __repr__(self):
        """ピザの構成引数を返す."""
        return f"Pizza(size={self.size},is_cheeze={self.is_cheeze},toppings={self.toppings})"
