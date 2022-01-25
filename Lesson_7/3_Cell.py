class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return str(f'Ячеек: {self.cell}')

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        return Cell(self.cell - other.cell)

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def make_order(self, count):
        a = self.cell
        while a > 0:
            for b in range(count):
                print("*", end="")
                a -= 1
                if a <= 0:
                    break
            print('\n', end="")

cell_1 = Cell(15)
cell_2 = Cell(10)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

print(cell_1.make_order(4))
