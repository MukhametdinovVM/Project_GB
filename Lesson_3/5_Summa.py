def my_sum():
    sum_result = 0
    ex = False
    while ex == False:
        number = input('Введите числа через пробел или значок "*" для выхода: ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == '*':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_result = sum_result + res
        print(f'Текущая сумма: {sum_result}')
    print(f'Финальный результат: {sum_result}')

my_sum()
