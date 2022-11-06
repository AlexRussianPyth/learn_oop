class HtmlElement:
    """Объект, представляющию HTML Элемент"""
    indent_size = 2

    def __init__(self, name: str = "", text: str = ""):
        self.name = name
        self.text = text
        self.elements = []

    def __str__(self):
        """Переопределенный магический метод, вызывающий нашу собственную реализацию"""
        return self.__str(0)

    def __str(self, indent):
        lines = []
        i = " " * (indent * self.indent_size)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            i1 = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{i1}{self.text}")

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f"{i}</{self.name}>")
        return "\n".join(lines)
