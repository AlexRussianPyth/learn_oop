from element import HtmlElement


class HtmlBuilder:
    """
    Объект, который занимается сложной операцией по построению HTML элементов
    """
    def __init__(self, root_name: str):
        self.root_name = root_name
        self.__root = HtmlElement(name=root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(
                HtmlElement(child_name, child_text)
                )

    def add_child_fluent(self, child_name, child_text):
        """Позволяет связывать добавление элементов в 'цепочку'"""
        self.__root.elements.append(
                HtmlElement(child_name, child_text)
                )
        return self

    def __str__(self):
        return str(self.__root)
