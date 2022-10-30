from move import MoveBehavior
from shoot import ShootBehavior


class Army:
    """Общий класс для войск"""
    def __init__(
            self,
            move_behavior: MoveBehavior,
            shoot_behavior: ShootBehavior
            ):
        self.move_behavior = move_behavior
        self.shoot_behavior = shoot_behavior

    def reload(self):
        print("Reloading guns")

    def perform_shooting(self):  # Делегируем поведение объекту-компоненту
        self.shoot_behavior.shoot()

    def perform_move(self):  # Делегируем поведение объекту-компоненту
        self.move_behavior.move()

    def set_shoot_behavior(self, new_shoot_behavior: ShootBehavior):
        self.shoot_behavior = new_shoot_behavior

    def set_move_behavior(self, new_move_behavior: MoveBehavior):
        self.move_behavior = new_move_behavior

