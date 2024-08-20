class OldTemperatureSensor:
    """既存の古い温度計センサーシステム.

    この古いクラスをcelsius.pyと同じセンサーのインターフェースとして提供したい.
    """

    def __init__(self, temperature):
        self.temperature = temperature

    def get_temperature_fahrenheit(self):
        return self.temperature
