from command import Command


class Kitchen:
    def get_order(self, order: Command):
        self.order = order

    def make_food(self):
        self.order.execute()
