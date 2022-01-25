from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def payment(self):
        pass

    def __str__(self):
        return f"Площадь равна: {self.payment}"

class Coat(Clothes):

    @property
    def payment(self):
        return self.param / 6.5 + 0.5

class Suit(Clothes):

    @property
    def payment(self):
        return self.param * 2 + 0.3

coat = Coat(92)
suit = Suit(1.76)

print(coat.payment)
print(suit.payment)
print(coat.payment + suit.payment)

