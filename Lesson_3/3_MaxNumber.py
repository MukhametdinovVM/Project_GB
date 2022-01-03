def my_func(arg1, arg2, arg3):
    if arg2 >= arg3 <= arg1:
        return arg1 + arg2
    elif arg2 < arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))

print(f'Результат - {my_func(number_1, number_2, number_3)}')
