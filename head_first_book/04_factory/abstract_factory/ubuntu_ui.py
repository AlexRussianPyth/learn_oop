class UbuntuWindow:
    """
    класс, симулирующий ui 'окно' в ubuntu
    """
    def __init__(self):
        self.description = "Ubuntu Window"
    
    def __str__(self):
        return f"Это {self.description}"


class UbuntuMenu:
    """
    класс, симулирующий ui 'Menu' в ubuntu
    """
    def __init__(self):
        self.description = "Ubuntu Menu"

    def __str__(self):
        return f"Это {self.description}"
