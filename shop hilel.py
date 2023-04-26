from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def get_name(self):
        pass


class Grecha(Item):
    def __init__(self):
        super().__init__(price=20)

    def get_name(self):
        return "гречка"


class Cookie(Item):
    def __init__(self):
        super().__init__(price=15)

    def get_name(self):
        return "печиво"


class Apple(Item):
    def __init__(self):
        super().__init__(price=10)

    def get_name(self):
        return "яблуко"

class Shop:
    def productt(self, product, price):
        if product == "гречка":
            return Grecha()
        elif product == "печиво":
            return Cookie()
        elif product == "яблуко":
            return Apple()
        else:
            raise ValueError("не правильне ім'я товару")
