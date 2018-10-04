__author__ = 'Сафин Ильшат'

# 6. В одномерном массиве найти сумму элементов, находящихся
# между минимальным и максимальным элементами. 
# Сами минимальный и максимальный элементы в сумму не включать.

import random

my_list = [random.randrange(0, 10) for i in range(10)]
new_list = sorted(my_list)
print(my_list)
# print(new_list)
min_i = new_list[0]
max_i = new_list[-1]
n_min_i = my_list.index(min_i)
n_max_i = my_list.index(max_i)
if n_min_i < n_max_i:
    new_list = my_list[n_min_i + 1:n_max_i]
elif n_max_i < n_min_i:
    new_list = my_list[n_max_i + 1:n_min_i]
print('Между min и max:', new_list)
print('min:', min_i, 'max:', max_i)
print('Сумма между min и max:', sum(new_list))
