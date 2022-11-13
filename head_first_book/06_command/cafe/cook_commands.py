from command import Command
from cooks import SushiCook, Shaurmist


class SushiCookMakeSushiOrder(Command):
    def __init__(self, cook: SushiCook):
        self.cook = cook

    def execute(self):
        self.cook.grind_knifes()
        self.cook.make_roll()


class ShaurmistMakeShaurmaOrder(Command):
    def __init__(self, cook: Shaurmist):
        self.cook = cook

    def execute(self):
        self.cook.smoke()
        self.cook.make_shaurma()
