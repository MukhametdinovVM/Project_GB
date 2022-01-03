def my_func(x, y):
    number_1 = x ** y
    number_2 = 1
    i = 1
    while i <= abs(y):
        number_2 *= x
        i += 1

    return number_1, 1 / number_2

number_1 = int(input('Число номер 1: '))
number_2 = int(input('Число номер 2: '))

print(my_func(number_1, number_2))