class Road:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def mass(self):
        self.weigth = 25
        self.tickness = 5
        mass = self.length * self.width * self.weigth * self.tickness / 1000
        print(f"Для строительства дороги необходимо: {mass}т.")

road_mass = Road(int(input("Укажите длину дороги: ")), int(input("Укажите ширину дороги: ")))
road_mass.mass()
