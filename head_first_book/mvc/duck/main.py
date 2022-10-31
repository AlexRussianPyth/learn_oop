from duck import RubberDuck, MallardDuck, Goose, GooseAdapter

if __name__ == '__main__':
    mallard = MallardDuck()
    rubber = RubberDuck()
    goose = Goose()
    adapted_goose = GooseAdapter(goose)

    ducks = [mallard, rubber, adapted_goose]

    for duck in ducks:
        duck.quack()
