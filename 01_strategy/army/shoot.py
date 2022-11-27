from abc import ABC, abstractmethod


class ShootBehavior(ABC):
    """Абстрактный метод, определяющий способы стрельбы"""
    @abstractmethod
    def shoot(self):
        pass


class ShootWithRifles(ShootBehavior):
    """Реализация Стрельбы"""
    def shoot(self):
        print("Rifle Shooting")


class ShootWithCannons(ShootBehavior):
    """Реализация Стрельбы"""
    def shoot(self):
        print("Take cannons and shoot!")
