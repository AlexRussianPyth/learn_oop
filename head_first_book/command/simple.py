import abc


class Command(abc.ABC):
    """Класс-интерфейс для паттерна Команда"""
    @abc.abstractmethod
    def execute(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light  # light - класс, управляющий светом

    def execute(self):
        self.light.on()

class Light:
    def on(self):
        print("Свет включается")


class SimpleRemoteControl:
    """Простой пульт с одним слотом для подключения устройств и одной кнопкой"""
    def set_command(self, command: Command):
        """Загрузить команду. Можно вызвать повторно, если захотим изменить команду"""
        self.slot = command

    def button_was_pressed(self):
        """Выполняем команду"""
        self.slot.execute()


class RemoteControlTest:
    def __init__(self):
        self.remote = SimpleRemoteControl()
        self.light = Light()
        self.light_on = LightOnCommand(self.light)


        self.remote.set_command(self.light_on)
        self.remote.button_was_pressed()


foo = RemoteControlTest()
