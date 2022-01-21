zamena = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open("text_4.txt") as file_obj:
    for i in file_obj:
        line = i.split(" ")
        # print(line)
        new_file.append(zamena[line[0]] + " — " + line[2])
    print(new_file)

with open('text_4_New.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)