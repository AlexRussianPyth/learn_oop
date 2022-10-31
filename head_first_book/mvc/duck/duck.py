from abc import ABC, abstractmethod


class Quackable(ABC):
    """Интерфейс класса, который умеет крякать"""
    @abstractmethod
    def quack(self):
        pass


class MallardDuck(Quackable):
    def quack(self):
        print("Quack!")


class RedheadDuck(Quackable):
    def quack(self):
        print("Quack!")


class DuckCall(Quackable):
    def quack(self):
        print("Kwak!")


class RubberDuck(Quackable):
    def quack(self):
        print("Squeak")


class Goose:
    def honk(self):
        print("Honk!")


class GooseAdapter(Quackable):
    def __init__(self, goose: Goose):
        self.goose = goose

    def quack(self):
        self.goose.honk()
