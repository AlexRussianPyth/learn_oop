from thing import Thing
from thermometers import CelsiusThermometer


class ClothesPicker:
    """Позволяет не ошибиться с выбором одежды под погоду на улице"""
    def __init__(
            self,
            clothes: list[Thing],
            celsius_thermometer: CelsiusThermometer):
        self.clothes = clothes
        self.thermometer = celsius_thermometer

    def __str__(self):
        return f"Мои вещи: {[thing.name for thing in self.clothes]}"

    def get_clothes_by_temp(self) -> list[Thing]:
        """Возвратит список вещей, которые подойдут под данную температуру"""
        suitable_clothes = []
        temperature = self.thermometer.get_temperature()
        print(temperature)

        for thing in self.clothes:
            # Если температура подходит для данной вещи - добавим в список
            temp_range = thing.celsius_temp_range
            if temp_range[0] <= temperature <= temp_range[1]:
                suitable_clothes.append(thing)

        return suitable_clothes
