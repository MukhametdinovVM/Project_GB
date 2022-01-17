from functools import reduce

def my_func(el_1, el):
    return el_1 * el

my_list = [el for el in range(99, 1001) if el % 2 ==0]
print(my_list)
work = reduce(my_func, my_list)
print(work)