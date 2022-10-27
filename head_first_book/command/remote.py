from command import Command


class SimpleRemoteControl:
    """Простой пульт с одним слотом для подключения устройств и одной кнопкой"""
    def set_command(self, command: Command):
        """Загрузить команду. Можно вызвать повторно, если захотим изменить команду"""
        self.slot = command

    def button_was_pressed(self):
        """Выполняем команду"""
        self.slot.execute()


class RemoteControl:
    """Пульт с подключаемым устройством, и кнопками включения/выключения"""
    def set_on_command(self, command: Command):
        self.on_command = command

    def set_off_command(self, command: Command):
        self.off_command = command

    def button_was_pressed(self):
        self.on_command.execute()

    def undo(self):
        self.off_command.execute()
