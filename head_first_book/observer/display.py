from abstract_classes import DisplayInterface, ObserverInterface, SubjectInterface
from weather import WeatherData


class CurrentConditionsDisplay(DisplayInterface, ObserverInterface):
    def __init__(self):
        self.temperature = float()
        self.humidity = float()
        self.pressure = float()
        self.weather_data: WeatherData = None

    def add_subject(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity

    def display(self):
        print(f'Current temp: {self.temperature}, current humidity: {self.humidity}')

