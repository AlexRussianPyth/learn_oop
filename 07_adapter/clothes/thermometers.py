from abc import ABC, abstractmethod
import random


class Thermometer(ABC):
    """Абстрактный интерфейс для различных термометров"""

    @abstractmethod
    def get_temperature(self):
        """Возвратит температуру окружающей среды"""
        pass


class CelsiusThermometer(Thermometer):
    def get_temperature(self) -> int:
        return random.randint(-30, 40)


class FarenheitThermometer(Thermometer):
    def get_temperature(self) -> int:
        return random.randint(-22, 104)


class FarenheitAdapter(CelsiusThermometer):
    """Позволяет адаптировать градусник"""
    def __init__(self, farenheit: FarenheitThermometer):
        self.farenheit = farenheit

    def get_temperature(self):
        farenheit_temperature = self.farenheit.get_temperature()
        celsius_temperature = (farenheit_temperature - 32) / 1.8
        return celsius_temperature
