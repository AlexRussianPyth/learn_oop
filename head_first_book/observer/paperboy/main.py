from publisher import Publisher
from readers import UsualReader, Businessman


publisher = Publisher()
usual_reader = UsualReader()
business_reader = Businessman()


if __name__ == '__main__':
    # Добавляем Субъект (publisher) для Наблюдателя (usual_reader)
    usual_reader.subscribe(publisher)
    # Субъект обновляет данные и оповещает всех Наблюдателей
    publisher.get_content_for_newspaper(
            'Giant Godzilla Destroys New York',
            'Yozhik Povesilsya',
            {'TESLA': 45, 'APPLE': 32.1}
            )
    usual_reader.read()
    business_reader.subscribe(publisher)
    publisher.get_content_for_newspaper(
            'Coca Cola is really white',
            'Kalambur',
            {'TESLA': 41.1, 'APPLE': 33.6, 'VAZ': 0.0}
            )
    usual_reader.read()
    business_reader.read()
