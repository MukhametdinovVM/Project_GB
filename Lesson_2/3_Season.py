months = ['Зима', 'Весна', 'Лето', 'Осень']
months_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}

month = int(input('Введите месяц года: '))
if month == 12 or 0 < month < 3:
    print(months[0])
    print(months_dict[1])
elif 6 > month > 2:
    print(months[1])
    print(months_dict[2])
elif 9 > month > 5:
    print(months[2])
    print(months_dict[3])
elif 12 > month > 8:
    print(months[3])
    print(months_dict[4])
else:
    print('Fail')
