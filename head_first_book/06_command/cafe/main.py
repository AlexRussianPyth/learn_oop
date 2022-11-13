from kitchen import Kitchen
from cooks import SushiCook
from cook_commands import SushiCookMakeSushiOrder


if __name__ == "__main__":
    # Создадим повара
    sushi_cook = SushiCook("Miogo", 27, "Makes great sushi")
    sushi_cook.brag()
    order = SushiCookMakeSushiOrder(sushi_cook)

    # Создадим кухню
    kitchen = Kitchen()
    kitchen.get_order(order)

    kitchen.make_food()
