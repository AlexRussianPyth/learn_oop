from beverage import Espresso, DarkRoast, Mocha, Soy


# Закажем обычный "пустой" кофе
beverage = Espresso()
print(beverage.cost())

# Создаем Черный кофе, добавляем 2 Мокки и Сою
beverage2 = DarkRoast()
beverage2 = Mocha(beverage2)
beverage2 = Mocha(beverage2)
beverage2 = Soy(beverage2)
print(f"My coffee: {beverage2.get_description()} costs: {beverage2.cost()}$")
