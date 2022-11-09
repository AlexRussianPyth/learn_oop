from abc import ABC, abstractmethod

from osx_ui import OsXWindow, OsXMenu
from ubuntu_ui import UbuntuWindow, UbuntuMenu


class UserInterfaceFactory(ABC):
    """
    Абстрактная Фабрика для создания UI в различных ОС
    """
    @abstractmethod
    def make_window(self):
        pass

    @abstractmethod
    def make_menu(self):
        pass


class OSXUserInterfaceFactory(UserInterfaceFactory):
    """
    Тип: Реальная фабрика. Создает элементы интерфейса для OS X
    """
    def make_window(self):
        return OsXWindow()

    def make_menu(self):
        return OsXMenu()


class UbuntuUserInterfaceFactory(UserInterfaceFactory):
    """
    Тип: Реальная фабрика. Создает элементы интерфейса для Ubuntu
    """
    def make_window(self):
        return UbuntuWindow()

    def make_menu(self):
        return UbuntuMenu()
