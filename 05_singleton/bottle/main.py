from bottle import Bottle


if __name__ == "__main__":
    bottle = Bottle.get_instance()

    bottle.drink(40)
    bottle.drink(800)
    bottle.drink(22)

    bottle2 = Bottle.get_instance()
    bottle2.drink(bottle2.get_volume())
