class Coffee:

    def prepare(self):
        self.boil_water()
        self.brew_coffee_grinds()
        self.pour_in_cup()
        self.add_sugar_and_milk()

    def boil_water(self):
        print('Boiling Water')

    def brew_coffee_grinds(self):
        print('Dripping coffee through filter')

    def pour_in_cup(self):
        print('Pouring into cup')

    def add_sugar_and_milk(self):
        print('Adding sugar and milk')
