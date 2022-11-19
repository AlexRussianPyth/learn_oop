from clothes import ClothesPicker
from thing import Thing


things = [
        Thing(name="Шляпа", celsius_temp_range=(-30, 15)),
        Thing(name="Брюки", celsius_temp_range=(0, 25)),
        Thing(name="Шуба", celsius_temp_range=(-30, -10)),
        Thing(name="Шорты", celsius_temp_range=(25, 40)),
        ]


picker = ClothesPicker(things)

if __name__ == "__main__":
    print(picker)
