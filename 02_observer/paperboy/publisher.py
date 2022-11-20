from abstract_classes import SubscriberInterface, PublisherInterface


class Publisher(PublisherInterface):
    """Реализация интерфейса Издателя"""
    def __init__(self):
        self.subscribers = []
        self.news = str()
        self.comedy = str()
        self.shares_info = dict()

    def register_subscriber(self, subscriber: SubscriberInterface):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: SubscriberInterface):
        self.subscribers.remove(subscriber)

    def issue_newspaper(self):
        for subscriber in self.subscribers:
            subscriber.update(self.news, self.comedy, self.shares_info)

    def _new_info_achieved(self):
        """Как только набралось материала на целую газету,
        рассылаем ее Подписчикам"""
        if self.subscribers:
            self.issue_newspaper()
        else:
            print('Подписчиков у нашей дерьмовой газетенки совсем и нету')

    def get_content_for_newspaper(
            self,
            news: str,
            comedy: str,
            shares_info: dict):
        """Тестовый метод, симулирующий получение данных для нашей газеты"""
        self.news = news
        self.comedy = comedy
        self.shares_info = shares_info
        self._new_info_achieved()
