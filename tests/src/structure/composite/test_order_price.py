from src.structure.composite.models.box import Box
from src.structure.composite.models.product import Product


def test_product_price():
    """Productが正しい価格を返すかのテスト."""
    product = Product("テスト商品", 1000)
    assert product.price == 1000, "Productの価格が正しくありません"


def test_box_price():
    """Box単品が正しい価格を返すかのテスト."""
    box = Box("テストボックス", 500)
    assert box.price == 500, "Boxの価格が正しくありません"


def test_box_with_products_price():
    """BoxにProductを追加して正しい合計価格を返すかのテスト."""
    box = Box("テストボックス", 500)
    product1 = Product("テスト商品1", 1000)
    product2 = Product("テスト商品2", 2000)
    box.add(product1)
    box.add(product2)
    assert box.price == 3500, "Boxに追加したProductの合計価格が正しくありません"


def test_box_with_box_and_products_price():
    """BoxにBoxとProductを追加して正しい合計金額を返すかのテスト."""
    outer_box = Box("外側ボックス", 300)
    inner_box = Box("内側ボックス", 200)
    product1 = Product("テスト商品1", 1000)
    product2 = Product("テスト商品2", 2000)

    inner_box.add(product1)
    outer_box.add(inner_box)
    outer_box.add(product2)

    assert (
        outer_box.price == 3500
    ), "Boxに追加したBoxとProductの合計価格が正しくありません"
