number = int(input('Введите произвольное целое число: '))

i = 0

while number > 10:
    number_x = number % 10
    number = number // 10
    if number_x > i:
        i = number_x
print(i)