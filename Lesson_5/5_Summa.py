my_file = open("text_5.txt", "w")

numbers = input(f"Введите числа через пробел: ")
my_file.writelines(numbers)
number = numbers.split()

sum = 0

for i in number:
    sum = sum + int(i)

print(f"Сумма чисел равна: {sum}")

my_file.close()
