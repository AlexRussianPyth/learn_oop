from builder import HtmlBuilder


if __name__ == "__main__":
    builder = HtmlBuilder('ul')
    builder.add_child('li', 'hello')
    builder.add_child('li', 'world')
    print(builder)

    # Вызовы API цепочкой
    builder = HtmlBuilder("p")
    builder.add_child_fluent("span", "love").add_child("span", "death")
    print(builder)
