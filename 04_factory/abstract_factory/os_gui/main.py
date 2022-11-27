from factories import OSXUserInterfaceFactory, UbuntuUserInterfaceFactory
from designer import UIDesigner


if __name__ == "__main__":
    # Создаем Фабрику для OSX
    osx_factory = OSXUserInterfaceFactory()
    designer = UIDesigner(osx_factory)
    ui = designer.create_ui()
    print(ui)

    # Создаем Фабрику для Ubuntu
    ubuntu_factory = UbuntuUserInterfaceFactory()
    designer2 = UIDesigner(ubuntu_factory)
    ui = designer2.create_ui()
    print(ui)
