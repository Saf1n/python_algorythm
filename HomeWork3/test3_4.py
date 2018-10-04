__author__ = 'Сафин Ильшат'

# 4. Определить, какое число в массиве встречается чаще всего.

import random

my_list = [random.randrange(1, 10) for i in range(10)]
print(my_list)
often_num = 0
num_of_often_num = 0
for i in range(len(my_list)):
    x = my_list.count(i)
    if x > num_of_often_num:
        num_of_often_num = x
        often_num = i
print(often_num, 'встречается чаще всего - ', my_list.count(often_num), 'раз(а)')
