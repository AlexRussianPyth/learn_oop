from abc import ABC, abstractmethod


class Command(ABC):
    """Интерфейс Команды"""
    @abstractmethod
    def execute(self):
        """Выполняем команду"""
        pass
