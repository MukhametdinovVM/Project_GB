proceeds = int(input('Введите сумму выручки: '))
costs = int(input('Введите сумму издержек: '))

profit = proceeds - costs

if profit > 0:
    print('Прибыль')
    profitability = profit * 100 // proceeds
    print(f'Рентабельность составляет: {profitability}%')
    people = int(input('Введите численность сотрудников фирмы: '))
    proceeds_people = proceeds // people
    print(f'Прибыль фирмы в расчёте на одного сотрудника: {proceeds_people}')
else:
    print('Убыток')