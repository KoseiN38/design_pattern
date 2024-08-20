from src.structure.adapter.models.celsius import TemperatureSensor
from src.structure.adapter.models.fahrenheit import OldTemperatureSensor


class TemperatureSensorAdapter(TemperatureSensor):
    """旧センサークラスを新クラスと同等のインターフェースを提供する.

    Args:
        TemperatureSensor (_type_): _description_
    """

    def __init__(self, old_sensor: OldTemperatureSensor):
        self.old_sensor = old_sensor

    def get_temperature_celsius(self):
        """TemperatureSensorと同じ関数名で提供するadapterパターン.

        Returns:
            _type_: _description_
        """
        fahrenheit = self.old_sensor.get_temperature_fahrenheit()
        celsius = (fahrenheit - 32) * 5 / 9
        return round(celsius, 1)
