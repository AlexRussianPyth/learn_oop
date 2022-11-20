class Amplifier:
    def set_volume(self, volume: int):
        self.volume = volume


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
        pass

    def move_down(self):
        pass


class HomeTheaterFacade:
    def __init__(
            self,
            amplifier,
            streaming_player,
            projector,
            lights,
            popcorn):
        self.amplifier = amplifier
        self.streaming_player = streaming_player
        self.projector = projector
        self.lights = lights
        self.popcorn = popcorn

    def watch_movie(self):
        pass

    def end_movie(self):
        pass
