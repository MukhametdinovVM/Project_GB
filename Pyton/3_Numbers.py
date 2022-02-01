class Numbers:

    def __init__(self):
        self.my_list = []

    def my_numb(self):

        while True:
            try:
                val = int(input("Введите значения: "))
                self.my_list.append(val)
                print(f"Cписок - {self.my_list} \n ")
            except:
                print(f"Недопустимое значение!")
                answer = input(f"Попробовать еще? Yes(Y) or No(N): ").upper()

                if answer == "Y":
                    continue
                elif answer == "N":
                    return f"Выход"
                else:
                    return f"Выход"


my_list = Numbers()
print(my_list.my_numb())
