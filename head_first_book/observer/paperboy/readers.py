from abstract_classes import (
        ReaderInterface,
        SubscriberInterface)
from publisher import Publisher


class UsualReader(ReaderInterface, SubscriberInterface):
    def __init__(self):
        self.news = str()
        self.comedy = str()
        self.shares_info = dict()
        self.publisher: Publisher = None

    def subscribe(self, publisher: Publisher):
        self.publisher = publisher
        self.publisher.register_subscriber(self)

    def update(self, news: str, comedy: str, shares_info: dict):
        self.news = news
        self.comedy = comedy

    def read(self):
        print(f'''This usual man knows news: {self.news},
                and jokes: {self.comedy}''')


class Businessman(ReaderInterface, SubscriberInterface):
    def __init__(self):
        self.news = str()
        self.comedy = str()
        self.shares_info = dict()
        self.publisher: Publisher = None

    def subscribe(self, publisher: Publisher):
        self.publisher = publisher
        self.publisher.register_subscriber(self)

    def update(self, news: str, comedy: str, shares_info: dict):
        self.news = news
        self.shares_info = shares_info

    def read(self):
        print(f'''This businessman knows news: {self.news},
        and shares: {self.shares_info}''')
