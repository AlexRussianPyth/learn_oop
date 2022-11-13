from abc import ABC, abstractmethod


class Command(ABC):
    """Класс-интерфейс для Паттерна Команда"""
    @abstractmethod
    def execute(self):
        """Выполняет внутренную логику"""
        pass

    @abstractmethod
    def undo(self):
        """Отменяет внутренную логику"""
        pass
