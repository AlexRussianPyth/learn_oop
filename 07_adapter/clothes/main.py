from clothes import ClothesPicker
from thing import Thing
from thermometers import (
        CelsiusThermometer,
        FarenheitThermometer,
        FarenheitAdapter
        )


things = [
        Thing(name="Шляпа", celsius_temp_range=(-30, 15)),
        Thing(name="Брюки", celsius_temp_range=(0, 25)),
        Thing(name="Шуба", celsius_temp_range=(-30, -10)),
        Thing(name="Шорты", celsius_temp_range=(25, 40)),
        ]

celsius = CelsiusThermometer()
farenheit = FarenheitThermometer()
adapter = FarenheitAdapter(farenheit)


picker1 = ClothesPicker(things, celsius)
picker2 = ClothesPicker(things, adapter)


if __name__ == "__main__":
    print(picker1.get_clothes_by_temp())
    print(picker2.get_clothes_by_temp())
