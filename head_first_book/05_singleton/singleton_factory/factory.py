from functools import lru_cache


class Singleton:
    """
    Класс, симулирующий обычный объект с данными и поведением
    """
    def __init__(self) -> None:
        self.state = "I am alive!"

    def set_state(self, state: str) -> None:
        self.state = state

    def get_state(self) -> str:
        return self.state


@lru_cache(maxsize=1)  # Так мы всегда будет отдавать Одиночку
def singleton_factory(singleton):
    """
    Фабрика, которая всегда отдает единственный экземпляр
    указанного объекта
    """
    return singleton()
