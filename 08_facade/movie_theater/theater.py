from devices import Amplifier, StreamingPlayer, Projector, Lights


class HomeTheaterFacade:
    def __init__(
            self,
            amplifier: Amplifier,
            streaming_player: StreamingPlayer,
            projector: Projector,
            lights: Lights,):
        self.amplifier = amplifier
        self.streaming_player = streaming_player
        self.projector = projector
        self.lights = lights

    def watch_movie(self):
        self.amplifier.volume = 10
        self.streaming_player.on()
        self.projector.move_down()
        self.lights.off()

    def end_movie(self):
        self.amplifier.volume = 0
        self.streaming_player.off()
        self.projector.move_up()
        self.lights.on()
