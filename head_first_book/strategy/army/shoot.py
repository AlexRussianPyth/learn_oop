from abc import ABC, abstractmethod


class ShootBehavior(ABC):
    """Абстрактный метод, определяющий способы стрельбы"""
    @abstractmethod
    def shoot(self):
        pass


class ShootWithRifles(ShootBehavior):
    def shoot(self):
        print("Rifle Shooting")


class ShootWithCannons(ShootBehavior):
    def shoot(self):
        print("Take cannons and shoot!")
