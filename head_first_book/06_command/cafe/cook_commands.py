from command import Command
from cooks import SushiCook


class SushiCookMakeSushiOrder(Command):
    def __init__(self, cook: SushiCook):
        self.cook = cook

    def execute(self):
        self.cook.grind_knifes()
        self.cook.make_roll()
