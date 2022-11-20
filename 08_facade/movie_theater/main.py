from theater import HomeTheaterFacade
from devices import Amplifier, StreamingPlayer, Projector, Lights


if __name__ == "__main__":
    theater = HomeTheaterFacade(
            amplifier=Amplifier(4),
            streaming_player=StreamingPlayer(),
            projector=Projector(),
            lights=Lights()
            )

    theater.watch_movie()
    theater.end_movie()
