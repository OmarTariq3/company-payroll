class Item:
    def __init__(self, desc, price_per_one, quantity):
        self.desc = desc
        self.price_per_one = price_per_one
        self.quantity = quantity

    @property
    def price(self):
        return self.price_per_one * self.quantity


class Book(Item):
    def __init__(self, desc, price_per_one, quantity, author):
        super().__init__(desc, price_per_one, quantity)
        self.desc = desc
        self.price_per_one = price_per_one
        self.quantity = quantity
        self.author = author


class Food(Item):
    def __init__(self, desc, price_per_one, quantity, expiration_date):
        super().__init__(desc, price_per_one, quantity)
        self.desc = desc
        self.price_per_one = price_per_one
        self.quantity = quantity
        self.author = expiration_date
