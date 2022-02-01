class Warehouse:

    def __init__(self, model, price, number, *args):
        self.model = model
        self.price = price
        self.number = number
        self.all = []

    def __str__(self):
        return f"На складе: {self.model}, в количестве: {self.number}шт., по цене: {self.price}$"


class Car(Warehouse):

    def __init__(self, model, price, number, max_speed):
        super().__init__(model, price, number)
        self.max_speed = max_speed

    def acceptance(self):

        try:
            mark = input(f"Введите марку: ")
            kolvo = int(input(f"Введите количество: "))
            tsena = int(input(f"Цена за автомобиль: "))
            self.list = {"Марка": mark, "Количество": kolvo, "Цена за автомобиль": tsena}
            self.all.append(self.list)
            print(f"Текущий список -\n {self.all}")
        except:
            print(f"Ошибка ввода данных")
            return Car.acceptance(self)

        no = input(f"Продолжить ввод? Yes(Y) or No(N): ").upper()
        if no == "N":
            print(f"На складе:\n {self.all}")
            return f"Все автомобили помещенны на склад!!!"
        else:
            return Car.acceptance(self)


class Civil(Car):

    def max_civil(self):
        return f"Максимальная скорость гражданского автомобиля {self.max_speed}"


class Racing(Car):

    def max_racing(self):
        return f"Максимальная скорость гоночного автомобиля {self.max_speed}"


class Special(Car):

    def max_special(self):
        return f"Максимальная скорость автомобиля специального назначения {self.max_speed}"


car_1 = Civil("Toyota", 2000, 5, 60)
car_2 = Racing("Ferrari", 1200, 5, 300)
car_3 = Special("Police", 1500, 1, 250)
print(car_1.acceptance())
print(car_1.max_civil())
print(car_2.max_racing())
print(car_3.max_special())
