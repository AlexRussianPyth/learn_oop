class OsXWindow:
    """
    класс, симулирующий ui 'Window' в OSX
    """
    def __init__(self):
        self.description = "OsX Window"

    def __str__(self):
        return f"Это {self.description}"


class OsXMenu:
    """
    класс, симулирующий ui 'Menu' в OSX
    """
    def __init__(self):
        self.description = "OsX Menu"

    def __str__(self):
        return f"Это {self.description}"
