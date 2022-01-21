class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки - {self.title}"

class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

pen = Pen("Ручкой")
pencil = Pencil("Карандашом")
handle = Handle("Маркером")

print(pen.draw())
print(pencil.draw())
print(handle.draw())
