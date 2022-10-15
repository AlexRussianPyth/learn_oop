from abc import ABC, abstractmethod


class FlyBehavior(ABC):

    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("Flyiiiinnng")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("Cannot fly!")


class QuackBehavior(ABC):

    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print('Quack!')


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak!")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("Silence")

class Duck:
    """Общий класс для уток"""
    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def swim(self):
        print("Утка плывет")

    def perform_quack(self):  # Делегируем поведение объекту-компоненту
        self.quack_behavior.quack()

    def perform_fly(self):
        self.fly_behavior.fly()

    @abstractmethod
    def display(self):
        pass


mullard_duck = Duck(FlyWithWings(), Squeak())

mullard_duck.perform_fly()
mullard_duck.perform_quack()
