class TemperatureSensor:
    """新しいシステムが期待するセンサークラス."""

    def __init__(self, temperature):
        self.temperature = temperature

    def get_temperature_celsius(self):
        return self.temperature
