class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


# Other Realisation
class Logger(object):
    _instance = None  # Классовая переменная, которая будет хранить единственный экземпляр

    def __init__(self):
        """Выглядит убогенько, но бывают и такие реализации.
        В данном случае мы запрещаем использовать конструктор экземпляра.
        """
        raise RuntimeError(f"Call {__class__.__name__}.instance() instead")

    @classmethod
    def instance(cls):
        """Метод для доступа к экземпляру-Одиночке"""
        if cls._instance is None:
            print('Создаем Новый Экземпляр')
            cls._instance = cls.__new__(cls)
        else:
            print("Возвращаем Существующий Экземпляр")
        return cls._instance


foo = Logger.instance()
print(foo)
foo2 = Logger.instance()
print(foo2)
