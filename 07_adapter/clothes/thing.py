from pydantic import BaseModel


class Thing(BaseModel):
    """
    Объект, представляющий Вещь в вашем гардеробе

    Данные:
    name название вещи
    celsius_temp_range диапазон формата (min, max), внутри которого нам
    рекомендуется носить данную вещь
    """
    name: str
    celsius_temp_range: tuple
