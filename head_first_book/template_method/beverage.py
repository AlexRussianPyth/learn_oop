from abc import ABC, abstractmethod


class CaffeineBeverage(ABC):
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print('Boiling Water')

    @abstractmethod
    def brew(self):
        pass

    def pour_in_cup(self):
        print('Pouring into cup')

    @abstractmethod
    def add_condiments(self):
        pass
