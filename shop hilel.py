from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def get_name(self):
        pass

class Grecha(Item):
    def get_name(self):
        return "гречка"

class Cookie(Item):
    def get_name(self):
        return "печиво"

class Apple(Item):
    def get_name(self):
        return "яблуко"

class Shop:
    def productt(self, product):
        if product == "гречка":
            return Grecha()
        elif product == "печиво":
            return Cookie()
        elif product == "яблуко":
            return Apple()
        else:
            raise ValueError("не правильне ім'я товару")
