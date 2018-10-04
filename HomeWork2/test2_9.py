__author__ = 'Сафин Ильшат'

# coding: utf-8

# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

n = int(input())
max_sum_1 = 0
max_n = 0
while n != 0:
    m = n
    sum_1 = 0
    while n > 0:
        sum_1 += (n % 10)
        n //= 10
    if sum_1 > max_sum_1:
        max_sum_1 = sum_1
        max_n = m
    n = int(input())
print('Число', max_n, 'имеет максимальную сумму цифр:', max_sum_1)
