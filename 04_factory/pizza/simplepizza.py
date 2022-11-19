class SimplePizzaFactory:
    def create_pizza(self, pizza_type: str):
        pizza = None
        if pizza_type == "veggie":
            pizza = Veggie()
        elif pizza_type == "meat":
            pizza = MeatPizza()
        return pizza


class Veggie:
    def __init__(self):
        self.description = "Veggie"


class MeatPizza:
    def __init__(self):
        self.description = "Meat Pizza"


class PizzaShop:
    def __init__(self, pizza_factory: SimplePizzaFactory):
        self.pizza_factory = pizza_factory

    def order_pizza(self, pizza_type: str):
        """Метод, позволяющий заказать конкретную пиццу"""
        pizza = self.pizza_factory.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
