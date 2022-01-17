from itertools import cycle
from itertools import count

a = 0
for el in cycle(input("Введите числа через пробел: ").split()):
    if a > 6:
        break
    print(el)
    a += 1

for el in count(int(input("Введите стартовое число меньше 10: "))):
    if el > 10:
        break
    else:
        print(el)
