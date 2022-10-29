from beverage import CaffeineBeverage


class Coffee(CaffeineBeverage):
    def _brew(self):
        print('Dripping coffee through filter')

    def _add_condiments(self):
        print('Adding sugar and milk')
