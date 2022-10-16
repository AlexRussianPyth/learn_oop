from abstract_classes import ObserverInterface, SubjectInterface, DisplayInterface


class WeatherData(SubjectInterface):
    
    def __init__(self):
        self.observers = []
        self.temperature = float()
        self.humidity = float()
        self.pressure = float()

    def register_observer(self, observer: ObserverInterface):
        self.observers.append(observer)

    def remove_observer(self, observer: ObserverInterface):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        """Тестовый метод, симулирующий получение данных с метеостанции"""
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()

