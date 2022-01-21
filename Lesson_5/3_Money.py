my_f = open("text_3.txt", "r", encoding="utf-8")

content = my_f.readlines()

money = 0

for line in content:
    words = line.split()
    money = money + float(words[1])
    if float(words[1]) < 20000:
        print(f"Сотрудник с зарплатой меньше 20000: {words[0]}")

pay = money / len(content)
print(f"Средняя зарплата сотрудника: {pay}")

my_f.close()
