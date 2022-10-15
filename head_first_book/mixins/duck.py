from abc import ABC

class Duck:
    pass


class FlyBehavior(ABS):

    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("Flyiiiinnng")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("Cannot fly!")


class QuackBehavior(ABS):

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

