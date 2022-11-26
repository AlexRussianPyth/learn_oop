from igloo_director import IglooDirector
from castle_director import CastleDirector
from houseboat_director import HouseBoatDirector


if __name__ == "__main__":
    # Строим разные варианты домов
    IGLOO = IglooDirector.construct()
    CASTLE = CastleDirector.construct()
    HOUSEBOAT = HouseBoatDirector.construct()

    print(IGLOO.construction())
    print(CASTLE.construction())
    print(HOUSEBOAT.construction())
