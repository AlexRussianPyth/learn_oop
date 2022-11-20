from duck import Duck, MallardDuck, WildTurkey, TurkeyAdapter


class TestDuck:
    """Класс для тестирования Уток"""
    def __init__(self, duck: Duck):
        self.duck = duck

    def test(self):
        self.duck.quack()
        self.duck.fly()


if __name__ == '__main__':
    real_duck = MallardDuck()
    first_test = TestDuck(real_duck)
    first_test.test()

    turkey = WildTurkey()
    false_duck = TurkeyAdapter(turkey)
    second_test = TestDuck(false_duck)
    second_test.test()
