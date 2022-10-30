from abc import ABC, abstractmethod


class MoveBehavior(ABC):
    """Абстрактный класс передвижения войск"""
    @abstractmethod
    def move(self):
        pass


class Running(MoveBehavior):
    def move(self):
        print('Running!')


class Walking(MoveBehavior):
    def move(self):
        print("Walking slowly")


class Standing(MoveBehavior):
    def move(self):
        print("Stand still")
