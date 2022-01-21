class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} поехала"
    def stop(self):
        return f"{self.name} остановилась"
    def turn(self, direction):
        return f"{self.name} повернула {direction}"

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Скорость авто {self.name} - {self.speed}")

        if self.speed > 60:
            return f"{self.name} - превысил скорость"
        else:
            return f"{self.name} - скорость разрешена"

class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Скорость авто {self.name} - {self.speed}")

        if self.speed > 40:
            return f"{self.name} - превысил скорость"
        else:
            return f"{self.name} - скорость разрешена"

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

toyota = TownCar(65, "Черная", "toyota", False)
print(toyota.speed, toyota.name, toyota.color, toyota.is_police)
print(toyota.go())
print(toyota.show_speed())
ferrari = SportCar(200, "Красная", "ferrari", False)
print(ferrari.speed, ferrari.name, ferrari.color, ferrari.is_police)
print(ferrari.turn("направо"))
scania = WorkCar(0, "Белая", "scania", False)
print(scania.speed, scania.name, scania.color, scania.is_police)
print(scania.stop())
print(scania.show_speed())
mustang = PoliceCar(90, "Синий", "mustang")
print(mustang.speed, mustang.name, mustang.color)
print(mustang.go())
