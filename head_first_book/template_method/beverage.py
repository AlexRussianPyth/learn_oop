from abc import ABC, abstractmethod


class CaffeineBeverage(ABC):
    def prepare(self):
        self._boil_water()
        self._brew()
        self._pour_in_cup()
        self._add_condiments()

    def _boil_water(self):
        print('Boiling Water')

    @abstractmethod
    def _brew(self):
        pass

    def _pour_in_cup(self):
        print('Pouring into cup')

    @abstractmethod
    def _add_condiments(self):
        pass
