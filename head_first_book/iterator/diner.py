from menu_item import MenuItem
from errors import MenuSizeException


class DinerMenu:
    def __init__(self, max_items: int = 6):
        self.max_items = max_items
        self.num_of_items = 0
        self.menu_items = []

    def add_item(self, menu_item: MenuItem):
        if self.num_of_items >= self.max_items:
            raise MenuSizeException('Sorry, menu is full')

        self.num_of_items += 1
        self.menu_items.append(menu_item)

    def get_menu_items(self):
        return self.menu_items

    
