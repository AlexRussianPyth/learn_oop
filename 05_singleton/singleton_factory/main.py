from factory import ConcreteClass, singleton_factory


if __name__ == "__main__":
    object1 = singleton_factory(ConcreteClass)
    print(object1.get_state())

    object2 = singleton_factory(ConcreteClass)
    object2.set_state("Love me tender")
    print(object1.get_state())

    is_equal = (id(object1) == id(object2))

    print("Это Одиночка") if is_equal else print("Это разные объекты")
