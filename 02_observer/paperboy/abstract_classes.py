from abc import ABC, abstractmethod


class SubscriberInterface(ABC):
    """Абстрактный интерфейт Подписчика, который предполагает,
    что Подписчики могут обновлять информацию"""
    @abstractmethod
    def update(self, news: str, comedy: str, shares_info: dict):
        pass


class PublisherInterface(ABC):
    """Абстрактные интерфейс Издателя. Издатель должен уметь регистрировать 
    Подписчиков, удалять их с рассылки, рассылать газеты
    """
    @abstractmethod
    def register_subscriber(self, subscriber: SubscriberInterface):
        pass

    @abstractmethod
    def remove_subscriber(self, subscriber: SubscriberInterface):
        pass

    @abstractmethod
    def issue_newspaper(self):
        pass


class ReaderInterface(ABC):
    @abstractmethod
    def read(self):
        pass
