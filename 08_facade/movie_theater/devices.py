class Amplifier:
    def __init__(self, volume: int):
        self.__volume = volume

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, level: int):
        self.__volume = level


class StreamingPlayer:
    def on(self):
        print("Streaming player on")

    def off(self):
        print("Streaming player off")

    def pause(self):
        print("Streaming player on pause")

    def play(self):
        print('Streaming player is playing')


class Projector:
    def move_up(self):
        print("Move projector up")

    def move_down(self):
        print("Move projector down")


class Lights:
    def on(self):
        print("Lights on")

    def off(self):
        print("Lights off")
