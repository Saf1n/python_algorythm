__author__ = 'Сафин Ильшат'

# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

my_list = [random.randrange(-10, 10) for i in range(10)]
print(my_list)
new_list = [x for x in my_list if x < 0]
print('Только отрицательные элементы:', new_list)
new_list = sorted(new_list)
max_neg = new_list[-1]
print('Значение:', max_neg, 'и место в списке:', my_list.index(max_neg))
