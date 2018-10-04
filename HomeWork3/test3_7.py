__author__ = 'Сафин Ильшат'

# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.

import random

my_list = [random.randrange(0, 10) for i in range(10)]
new_list = sorted(my_list)
print(my_list)
min_1 = new_list[0]
min_2 = new_list[1]
print('Минимум №1:', min_1)
print('Минимум №2:', min_2)
