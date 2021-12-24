distance_start = int(input('Дистанция в первый день: '))
distance_max = int(input('Необходимая дистанция: '))

i = 1
distance = distance_start

while distance < distance_max:
    i += 1
    distance = distance + distance * 0.1
print(f'На {i} день спортсмен достиг результата — не менее {distance_max} км.')