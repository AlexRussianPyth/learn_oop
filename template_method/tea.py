from beverage import CaffeineBeverage


class Tea(CaffeineBeverage):
    def _brew(self):
        print('Steeping the tea')

    def _add_condiments(self):
        print('Adding Lemon')

