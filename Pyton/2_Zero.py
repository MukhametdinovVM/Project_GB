class Zero:
    def __init__(self, delimoe, delitel):
        self.delimoe = delimoe
        self.delitel = delitel

    @staticmethod
    def delenie(delimoe, delitel):
        try:
            return delimoe / delitel
        except ZeroDivisionError:
            return f"Делить на ноль нельзя"


delen = Zero(5, 8)
print(delen.delenie(5, 10))
print(Zero.delenie(5, 0))