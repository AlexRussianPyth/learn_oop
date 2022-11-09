class Bottle:
    """
    Класс-Одиночка. Вы с компанией собутыльников купили себе
    бутылочку горячительного на последние гроши...
    """
    _instance = None

    def __init__(self):
        """Запрещаем данный метод"""
        raise RuntimeError(f"Используйте {__class__.__name__}.get_instance()")

    @classmethod
    def get_instance(cls):
        """Покупает бутылку, или возвращает уже купленную"""
        if cls._instance == None:
            print("Братан, сгоняй за бутылочкой")
            cls._instance = cls.__new__(cls)
            cls._instance.volume = 500
        else:
            print("Мы же уже купили, братан")
        return cls._instance

    def drink(self, size: int):
        """Метод позволяет отпить из бутылки"""
        if size > self.volume:
            print("Куда хлебало раззявил? Другим оставь")
        elif size == self.volume:
            print("Допил подчистую, подлец")
            self.volume = self.volume - size
        else:
            print("Отхлебнул, браток?")
            self.volume = self.volume - size

    def get_volume(self):
        """Позволяет узнать, сколько жидкости осталось в бутылке"""
        return self.volume
