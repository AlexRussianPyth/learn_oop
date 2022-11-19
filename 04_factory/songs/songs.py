from enum import Enum
from uuid import UUID


class SongFormat(Enum):
    JSON = "JSON"
    XML = "XML"


class Song:
    def __init__(self, song_id: UUID, title: str, artist: str):
        self.song_id = song_id
        self.title = title
        self.artist = artist
