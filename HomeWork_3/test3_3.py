__author__ = 'Сафин Ильшат'

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

my_list = [random.randrange(1, 10) for i in range(10)]
my_min = 9
my_max = 0
for i in range(len(my_list)):
    if my_list[i] < my_min:
        my_min = my_list[i]
        i_min = i
    elif my_list[i] > my_max:
        my_max = my_list[i]
        i_max = i
print('Было:', my_list)
print('min:', my_min)
print('max:', my_max)
print(i_min, i_max)
my_list[i_min], my_list[i_max] = my_list[i_max], my_list[i_min]
print('Стало:', my_list)
