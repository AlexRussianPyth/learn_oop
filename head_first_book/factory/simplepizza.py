class SimplePizzaFactory:
    def create_pizza(pizza_type: str):
        pizza = None
        if pizza_type == 'veggie':
            pizza = Veggie()
        elif pizza_type == 'meat':
            pizza = MeatPizza()
        return pizza


class PizzaShop:
    def __init__(self, pizza_factory):
        self.pizza_factory = pizza_factory

    def order_pizza(self, pizza_type: str):
        """Метод, позволяющий заказать конкретную пиццу"""
        pizza = self.pizza_factory.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        returnn pizza
