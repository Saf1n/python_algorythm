__author__ = 'Сафин Ильшат'

# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. 
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее 
# последнюю ячейку. В конце следует вывести полученную матрицу.

matrix = [[int(input()) for _ in range(4)] for _ in range(3)]

sum_column = [0] * len(matrix[0])

for line in matrix:
    sum_line = 0

    for i, item in enumerate(line):
        sum_line += item
        sum_column[i] += item

        print(f'{item:>5}', end='')

    print(f'   {sum_line}')
