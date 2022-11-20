import abc


class Duck(abc.ABC):
    """Интерфейс для Утки"""
    @abc.abstractmethod
    def quack(self):
        pass

    @abc.abstractmethod
    def fly(self):
        pass


class Turkey(abc.ABC):
    """Абстрактный интерфейс для индюшки"""
    @abc.abstractmethod
    def gobble(self):
        """Умеет жрать"""
        pass

    @abc.abstractmethod
    def fly(self):
        """Могут летать, но недалеко"""
        pass


class MallardDuck(Duck):
    def quack(self):
        print("Кряк!")

    def fly(self):
        print("Я лечу!")


class WildTurkey(Turkey):
    def gobble(self):
        print("Gobble gobble")

    def fly(self):
        print("I'm flying a short distance(((")


"""В первую очередь реализовываем интерфейс Клиента. Допустим, нам придется
подменить часть уток индюшками, Клиентом будет Утка, которая хочет подключить
к себе внешний ресурс - Индюшку"""


class TurkeyAdapter(Duck):
    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for _ in range(5):
            # Наша Индюшка старается соответствовать и летит по чуть-чуть
            self.turkey.fly()
