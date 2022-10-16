from abc import ABC, abstractmethod


class ObserverInterface(ABC):

    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        pass


class SubjectInterface(ABC):
    @abstractmethod
    def register_observer(self, observer: ObserverInterface):
        pass
 
    @abstractmethod
    def remove_observer(self, observer: ObserverInterface):
        pass
    
    @abstractmethod
    def notify_observers(self):
        pass
        

class DisplayInterface(ABC):
    
    @abstractmethod
    def display(self):
        pass

