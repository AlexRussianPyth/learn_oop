from menu_item import MenuItem


class PancakeHouseMenu:
    def __init__(self):
        self.menu_items = []

    def add_item(self, item: MenuItem):
        self.menu_items.append(item)

    def get_menu_items(self):
        return self.menu_items
