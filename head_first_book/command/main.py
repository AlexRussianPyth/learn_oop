from remote import SimpleRemoteControl, RemoteControl
from devices import (GarageDoor, 
        GarageDoorOnCommand, 
        Light, 
        LightOnCommand, 
        LightOffCommand, 
        Stereo, 
        LoudStereoOnWithDVDCommand
        )

light_command = LightOnCommand(Light())
garage_command = GarageDoorOnCommand(GarageDoor())

remote = SimpleRemoteControl()

# Загружаем в пульт первую команду
remote.set_command(light_command)
remote.button_was_pressed()

# Меняем встроенную команду
remote.set_command(garage_command)
# Запускаем ее таким же образом
remote.button_was_pressed()

# Запустим пульт посложнее
light = Light()
remote2 = RemoteControl()
# Загрузим команды
remote2.set_on_command(LightOnCommand(light))
remote2.set_off_command(LightOffCommand(light))

remote2.button_was_pressed()
remote2.undo()

# Врубим стерео
stereo = Stereo()
loud_command = LoudStereoOnWithDVDCommand(stereo)

remote.set_command(loud_command)
remote.button_was_pressed()

print(stereo.__dict__)

