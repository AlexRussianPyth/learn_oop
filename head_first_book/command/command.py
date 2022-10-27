import abc


class Command(abc.ABC):
    """Класс-интерфейс для паттерна Команда"""
    @abc.abstractmethod
    def execute(self):
        pass
    
    @abc.abstractmethod
    def undo(self):
        pass
