from abc import ABC, abstractmethod


class Beverage(ABC):
    """Абстрактный класс-Напиток"""
    def __init__(self):
        self.description = "Unknown Beverage"

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass


class CondimentDecorator(Beverage, ABC):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    @abstractmethod
    def get_description(self):
        pass


class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"

    def cost(self):
        return 1.99


class DarkRoast(Beverage):
    def __init__(self):
        self.description = "Dark Roast Coffee"

    def cost(self):
        return 0.99


class Decaf(Beverage):
    def __init__(self):
        self.description = "Decaffeinded Coffee"

    def cost(self):
        return 1.05


class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House Blend Coffee"

    def cost(self):
        return 0.89


class Milk(CondimentDecorator):
    def cost(self):
        return 12

    def get_description(self):
        return 'love and sex'


class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return self.beverage.cost() + 0.20


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Soy"

    def cost(self):
        return self.beverage.cost() + 0.3
