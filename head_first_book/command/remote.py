from command import Command


class SimpleRemoteControl:
    """Простой пульт с одним слотом для подключения устройств и одной кнопкой"""
    def set_command(self, command: Command):
        """Загрузить команду. Можно вызвать повторно, если захотим изменить команду"""
        self.slot = command

    def button_was_pressed(self):
        """Выполняем команду"""
        self.slot.execute()

    def cancel(self):
        """Отменяем команду"""
        self.slot.undo()


class RemoteControl:
    """Пульт с подключаемым устройством, и кнопками включения/выключения"""
    def set_on_command(self, command: Command):
        self.on_command = command

    def set_off_command(self, command: Command):
        self.off_command = command

    def press_on_button(self):
        self.on_command.execute()

    def press_off_button(self):
        self.off_command.execute()
