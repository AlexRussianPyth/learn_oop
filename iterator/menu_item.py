class MenuItem:
    def __init__(self, name: str, description: str, vegetarian: bool, price: float):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def is_vegetarian(self):
        return self.vegetarian

    def get_price(self):
        return self.price
    
    def __repr__(self):
        return f'Item: {self.name} with price: {self.price}'

    def __str__(self):
        return f'Item: {self.name} with price: {self.price}'
