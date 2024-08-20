import argparse

from src.structure.adapter.factory.temperature_adapter import TemperatureSensorAdapter
from src.structure.adapter.models.celsius import TemperatureSensor
from src.structure.adapter.models.fahrenheit import OldTemperatureSensor
from src.structure.adapter.process.display_process import NewTemperatureSystem


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fahrenheit", type=float, help="Name of the user")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    # 実行引数の読み取り
    args = get_parser()

    # 古いセンサーを新しいセンサーにadapterする
    old_sensor = OldTemperatureSensor(args.fahrenheit)
    adapter = TemperatureSensorAdapter(old_sensor)
    new_sensor = NewTemperatureSystem(adapter)
    a = new_sensor.display_temperature()

    # 元の新しいセンサーをそのまま用いる
    base_new_sensor = NewTemperatureSystem(
        TemperatureSensor(
            round((args.fahrenheit - 32) * 5 / 9, 1),
        )
    )
    b = base_new_sensor.display_temperature()

    # 両者の結果が一致することを確認する
    assert a == b, f"not equal {a}, {b}"
