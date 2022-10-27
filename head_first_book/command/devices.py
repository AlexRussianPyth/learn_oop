from command import Command
from errors import UnidentifiedVolumeException


class GarageDoor:
    
    def __init__(self):
        pass

    def up(self):
        print("Garage Door Up")

    def down(self):
        print("Garage Door Down")

    def stop(self):
        print("Garage Door Stopped")

    def lightOn(self):
        print("Light in garage is on")

    def lightOff(self):
        print("Light in garage is off")


class GarageDoorOnCommand:
    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.up()


class GarageDoorOffCommand:
    """Объект-Команда для опускания гаражной двери"""
    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.down()


class Light:
    def on(self):
        print("Light is on")
    
    def off(self):
        print("Light is off")


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light  # light - класс, управляющий светом

    def execute(self):
        self.light.on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light  # light - класс, управляющий светом

    def execute(self):
        self.light.off()


class Stereo:
    def __init__(self, disc="cd", volume: int = 5):
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
