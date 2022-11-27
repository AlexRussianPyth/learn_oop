from factories import UserInterfaceFactory


class UIDesigner:
    """
    Занимается созданием элементов интерфейса внутри нашей OS
    """
    def __init__(self, ui_factory: UserInterfaceFactory) -> None:
        self.ui_factory = ui_factory

    def create_ui(self) -> tuple:
        """Возвращает созданные элементы"""
        return (self.ui_factory.make_window(), self.ui_factory.make_menu())
