from uuid import uuid4

from songs import SongFormat, Song
from serializers import SongSerializer

# Создадим песни
song1 = Song(uuid4(), "Welcome to USSR", "Beatles")
song2 = Song(uuid4(), "Back to Black", "Amy Winehouse")

# Создаем сериализатор
serializer = SongSerializer()

json_format = serializer.serialize(song1, SongFormat.JSON)
xml_format = serializer.serialize(song1, SongFormat.XML)
print(json_format)
print(xml_format)
