from thing import Thing


class ClothesPicker:
    """Позволяет получить одежду"""
    def __init__(self, clothes: list[Thing]):
        self.clothes = clothes

    def __str__(self):
        return f"Мои вещи: {[thing.name for thing in self.clothes]}"

