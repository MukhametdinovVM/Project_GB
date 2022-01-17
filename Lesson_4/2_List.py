list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list = [el for num, el in enumerate(list_1) if list_1[num] > list_1[num-1] and list_1[num] != list_1[0]]
print(f'Исходный список {list_1}')
print(f'Новый список {my_list}')
