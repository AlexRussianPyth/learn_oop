from army import Army
from shoot import ShootWithRifles, ShootWithCannons
from move import Running, Standing


# Полководец получает Армию
soldiers_army = Army(
            move_behavior=Running(),
            shoot_behavior=ShootWithRifles()
            )


if __name__ == "__main__":
    # Начинаем боевые действия
    soldiers_army.reload()
    soldiers_army.perform_shooting()
    soldiers_army.perform_move()

    # Солдаты устают, их заменяют артиллеристы
    soldiers_army.set_shoot_behavior(ShootWithCannons())
    soldiers_army.set_move_behavior(Standing())

    # Продолжаем воеватьол
    soldiers_army.reload()
    soldiers_army.perform_shooting()
    soldiers_army.perform_move()
