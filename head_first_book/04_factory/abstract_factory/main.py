from factories import OSXUserInterfaceFactory, UbuntuUserInterfaceFactory


if __name__ == "__main__":
    # Создаем Фабрику для OSX
    osx_factory = OSXUserInterfaceFactory()
    osx_window = osx_factory.make_window()
    osx_menu = osx_factory.make_menu()

    print(osx_window)
    print(osx_menu)

    # Создаем Фабрику для Ubuntu
    ubuntu_factory = UbuntuUserInterfaceFactory()
    ubuntu_window = ubuntu_factory.make_window()
    ubuntu_menu = ubuntu_factory.make_menu()

    print(ubuntu_window)
    print(ubuntu_menu)
