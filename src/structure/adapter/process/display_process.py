from src.structure.adapter.factory.temperature_adapter import TemperatureSensorAdapter
from src.structure.adapter.models.celsius import TemperatureSensor


class NewTemperatureSystem:
    """新旧センサーを扱うインターフェースとなるクラス."""

    def __init__(self, sensor: TemperatureSensorAdapter | TemperatureSensor):
        """センサークラスを初期化する.

        Args:
            sensor (TemperatureSensorAdapter | TemperatureSensor): 新クラスならそのまま用いて、旧クラスならadapterパターンのクラスを用いる
        """
        self.sensor = sensor

    def display_temperature(self):
        temp = self.sensor.get_temperature_celsius()
        print(f"体温は {temp}°C です。")
        return temp
