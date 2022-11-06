import json
import xml.etree.ElementTree as et

from songs import Song, SongFormat


def serialize_song_to_json(song: Song):
    """Превращает Песню в текстовый JSON формат"""
    song_info = {
        'id': str(song.song_id),
        'title': song.title,
        'artist': song.artist
        }
    return json.dumps(song_info)


def serialize_song_to_xml(song: Song):
    """Превращает Песню в текстовый XML формат"""
    song_info = et.Element('song', attrib={'id': str(song.song_id)})

    title = et.SubElement(song_info, 'title')
    title.text = song.title

    artist = et.SubElement(song_info, 'artist')
    artist.text = song.artist

    return et.tostring(song_info, encoding='unicode')


def get_serializer(target_format: SongFormat):
    if target_format == SongFormat.JSON:
        return serialize_song_to_json
    elif target_format == SongFormat.XML:
        return serialize_song_to_xml
    else:
        raise ValueError(target_format)


class SongSerializer:
    """
    Класс, которые превращает песни в строковые форматы
    """
    def serialize(self, song: Song, target_format: SongFormat):
        serializer = get_serializer(target_format)
        return serializer(song)
