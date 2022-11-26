from menu_item import MenuItem
from pancake import PancakeHouseMenu
from diner import DinerMenu
from items_data import pancake_data, diner_data


# Заводим меню тортов
pancake_menu = PancakeHouseMenu()
for item in pancake_data:
    pancake_menu.add_item(MenuItem(*item))

print(pancake_menu.get_menu_items())

# Заводим вечернее меню
diner_menu = DinerMenu()
for item in diner_data:
    diner_menu.add_item(MenuItem(*item))

print(diner_menu.get_menu_items())
