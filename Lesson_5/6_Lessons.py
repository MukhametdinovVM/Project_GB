slov = {}

my_file = open("text_6.txt", "r", encoding="utf-8")
string = my_file.readlines()

for line in string:
    # lesson, lecture, practice, lab = line.split(",")
    lesson = line.split(":")
    text = lesson[1].split()
    n = ""
    numbers = []
    for numb in line:
        if numb.isdigit():
            n += numb
            # print(numb)
        else:
            if n != "":
                numbers.append(int(n))
                n = ""
                # print(numbers)
                z = sum(numbers)
    slov[lesson[0]] = z
    # slov[lesson] = int(lecture)+int(practice)+int(lab)
    # print(f"{lesson} = {lecture}, {practice}, {lab}")
    # print(f"{lesson}")
    # print(f"{lesson[0]} - {z}")
print(slov)
my_file.close()
