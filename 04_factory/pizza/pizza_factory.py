from abc import ABC, abstractmethod


class PizzaStore(ABC):
    def __init__(self, pizza_factory):
        self.pizza_factory = pizza_factory

    def order_pizza(self, pizza_type: str):
        """Метод, позволяющий заказать конкретную пиццу"""
        pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type):
        pass
