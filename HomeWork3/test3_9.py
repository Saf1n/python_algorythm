__author__ = 'Сафин Ильшат'

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

print('Введите 12 цифр:')
matrix = [[int(input()) for _ in range(4)] for _ in range(3)]
for i in range(3):
    print(matrix[i])

mx = -1
for i in range(3):
    mn = 10
    for j in range(4):
        if matrix[i][j] < mn:
            mn = matrix[i][j]
    if mn > mx:
        mx = mn
print('Максимальный элемент среди минимальных:', mx)
