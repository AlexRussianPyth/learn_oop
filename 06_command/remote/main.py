from remote import SimpleRemoteControl, RemoteControl
from devices import (
        GarageDoor,
        GarageDoorOnCommand,
        Light,
        LightOnCommand,
        LightOffCommand,
        Stereo,
        LoudStereoOnWithDVDCommand
        )


if __name__ == "__main__":
    # Создаем Команды
    light_command = LightOnCommand(Light())
    garage_command = GarageDoorOnCommand(GarageDoor())

    # Создаем простой пульт управления с одной кнопкой и загружаем Команду
    remote = SimpleRemoteControl()
    remote.set_command(light_command)
    remote.button_was_pressed()

    # Меняем встроенную команду
    remote.set_command(garage_command)
    remote.button_was_pressed()

    # Запустим пульт посложнее
    light = Light()
    remote2 = RemoteControl()
    # Загрузим команды
    remote2.set_on_command(LightOnCommand(light))
    remote2.set_off_command(LightOffCommand(light))

    remote2.press_on_button()
    remote2.press_off_button()

    # Врубим стерео
    stereo = Stereo()
    loud_command = LoudStereoOnWithDVDCommand(stereo)

    remote.set_command(loud_command)
    remote.button_was_pressed()

    print(stereo.__dict__)

    remote.cancel()
    print(stereo.__dict__)
