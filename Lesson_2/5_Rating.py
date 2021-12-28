my_list = [7, 5, 3, 3, 1]

number = None

while number != 'end':
        number = input('Введите число: ')
        for i in range(len(my_list)):
                if number == 'end':
                        break
                elif int(number) > my_list[0]:
                        my_list.insert(0, int(number))
                elif int(number) < my_list[-1]:
                        my_list.append(int(number))
                elif my_list[i] > int(number) > my_list[i + 1]:
                        my_list.insert(i + 1, int(number))

print(f'Результат: {my_list}')
