from abc import ABC


class Cook(ABC):
    """Абстрактое представление Повара"""
    def __init__(self, name: str, age: int, proficiency: str):
        self.name = name
        self.age = age
        self.proficiency = proficiency

    def brag(self):
        """Похвалиться о себе"""
        print(f"I am {self.name},{self.age}, and i can {self.proficiency}")


class SushiCook(Cook):
    """Повар-сушист"""
    def make_roll(self):
        print("Make tasty fish roll")

    def grind_knifes(self):
        print("Grind his knifes")


class Shaurmist(Cook):
    """Дагестанский чудотворец"""
    def make_shaurma(self):
        print("Вааай, какая шаурмааа")

    def smoke(self):
        print("Красиво курит")
