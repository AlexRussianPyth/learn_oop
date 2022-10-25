import abc


class Command(abc.ABC):
    @abc.abstractmethod
    def execute(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light  # light - класс, управляющий светом

    def execute(self):
        self.light.on()

