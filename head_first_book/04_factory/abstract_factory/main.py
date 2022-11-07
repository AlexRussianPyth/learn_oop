from abc import ABC, abstractmethod


class UserInterfaceFactory(ABC):
    """Абстрактная Фабрика для создания UI в различных ОС"""
    @abstractmethod
    def make_window(self):
        pass

    @abstractmethod
    def make_menu(self):
        pass


class OSXUserInterfaceFactory(UserInterfaceFactory):
    def make_window(self):
        return OsXWindow()

    def make_menu(self):
        return OsXMenu()


class UbuntuUserInterfaceFactory(UserInterfaceFactory):
    def make_window(self):
        return UbuntuWindow()

    def make_menu(self):
        return UbuntuMenu()



# Фабрика Солярис



# Окно



# Меню
