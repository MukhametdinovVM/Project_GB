def fact():
    factor = 1
    for num in range(2, n + 1):
        factor *= num
        yield factor

a = 0
n = int(input("Введите число для вычисления факториала: "))

for el in fact():
    if a > 40:
        break
    print(el)
    a += 1
