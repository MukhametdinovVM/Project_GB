my_file = open("test.txt", "w")

line = input(f"Введите текст: ")

while line:
    my_file.writelines(line + "\n")
    line = input(f"Введите текст: ")
    if not line:
        break

my_file.close()

my_file = open("test.txt", "r")
content = my_file.read()
print(content)

my_file.close()
