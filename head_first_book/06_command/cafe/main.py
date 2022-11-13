from kitchen import Kitchen
from cooks import SushiCook, Shaurmist
from cook_commands import SushiCookMakeSushiOrder, ShaurmistMakeShaurmaOrder


if __name__ == "__main__":
    # Создадим поваров
    sushi_cook = SushiCook("Miogo", 27, "Makes great sushi")
    sushi_cook.brag()

    shaurmist = Shaurmist("Vaha", 50, "Paltchiki oblizhesh!")
    shaurmist.brag()

    order = SushiCookMakeSushiOrder(sushi_cook)
    order2 = ShaurmistMakeShaurmaOrder(shaurmist)

    # Создадим кухню
    kitchen = Kitchen()
    kitchen.get_order(order)
    kitchen.make_food()

    kitchen.get_order(order2)
    kitchen.make_food()
