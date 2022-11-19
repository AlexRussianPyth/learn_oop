from command import Command
from errors import UnidentifiedVolumeException


class GarageDoor:
    """Гаражная дверь нашего умного дома"""
    def up(self):
        print("Garage Door Up")

    def down(self):
        print("Garage Door Down")

    def stop(self):
        print("Garage Door Stopped")

    def light_on(self):
        print("Garage light is on")

    def light_off(self):
        print("Garage light is off")


class GarageDoorOnCommand(Command):
    """Объект Команды, которые открывает гаражную дверь"""
    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.up()

    def undo(self):
        self.garage_door.down()


class GarageDoorOffCommand(Command):
    """ Объект-Команда для опускания гаражной двери"""
    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.down()

    def undo(self):
        self.garage_door.up()


class Light:
    """ Класс, который определяет свет в нашем умном доме"""
    def on(self):
        print("Light is on")

    def off(self):
        print("Light is off")


class LightOnCommand(Command):
    """Команда, которая включит свет"""
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):
    """Команда, которая выключит свет"""
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class Stereo:
    """Стерео-система нашего умного дома"""
    def __init__(self, disc: str = "cd", volume: int = 5):
        self.disc = disc
        self.volume = volume

    def on(self):
        print("Стерео работает")

    def off(self):
        print("Стерео выключено")

    def set_cd(self):
        self.disc = "cd"

    def set_dvd(self):
        self.disc = "dvd"

    def set_volume(self, volume: int):
        if volume >= 1 and volume <= 10:
            self.volume = volume
        else:
            raise UnidentifiedVolumeException


class LoudStereoOnWithDVDCommand(Command):
    """Мультикоманда, которая громко включит dvd диск"""
    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()
        self.stereo.set_dvd()
        self.stereo.set_volume(10)

    def undo(self):
        self.stereo.off()
        self.stereo.set_volume(5)
