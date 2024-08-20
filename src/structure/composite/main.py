from src.structure.composite.models.box import Box
from src.structure.composite.models.product import Product

if __name__ == "__main__":
    # 製品を作成
    keyboard = Product("キーボード", 5000)
    mouse = Product("マウス", 3000)
    monitor = Product("モニター", 20000)

    # 小さな箱を作成し、製品を追加
    accessories_box = Box("アクセサリー箱", 500)
    accessories_box.add(keyboard)
    accessories_box.add(mouse)

    # 大きな箱を作成し、モニターと小さな箱を追加
    main_box = Box("メイン箱", 1000)
    main_box.add(monitor)
    main_box.add(accessories_box)

    # 注文内容を表示
    print("注文内容:")
    main_box.display()

    # 注文の合計価格を計算
    total_price = main_box.price
    print(f"\n注文の合計価格: {total_price}円")
