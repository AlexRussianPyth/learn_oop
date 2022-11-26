from abc import ABC, abstractmethod


class CaffeineBeverage(ABC):
    def prepare(self):
        """Это и есть Шаблонный Метод - это метод и это шаблон для алгоритма"""
        self._boil_water()
        self._brew()
        self._pour_in_cup()
        self._add_condiments()

    def _boil_water(self):
        """Метод кипячения воды - он не должен переопределяться"""
        print('Boiling Water')

    @abstractmethod
    def _brew(self):
        """Метод заваривания - должен переопределяться в классах-наследниках"""
        pass

    def _pour_in_cup(self):
        """Метод наливания в чашку - не должен переопределяться"""
        print('Pouring into cup')

    @abstractmethod
    def _add_condiments(self):
        """Метод добавления приправ - должен переопределиться"""
        pass
