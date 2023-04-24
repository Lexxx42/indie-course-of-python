# Обход элементов матрицы - 4
# Задана целочисленная матрица, состоящая из N строк и M столбцов. Необходимо обойти элементы этой матрицы слева направо снизу вверх и вывести элементы именно в таком порядке в виде таблицы.
#
# Программа принимает на вход два натуральных числа N и M – количество строк и столбцов матрицы. В каждой из последующих N строк записаны M целых чисел – элементы матрицы.
#
# Sample Input 1:
#
# 3 4
# 5 9 2 6
# 6 2 4 3
# 1 2 8 7
# Sample Output 1:
#
# 1 2 8 7
# 6 2 4 3
# 5 9 2 6
#
# Sample Input 2:
#
# 4 2
# 1 5
# 6 3
# 8 6
# 3 9
# Sample Output 2:
#
# 3 9
# 8 6
# 6 3
# 1 5

n, m = map(int, input().split())
matrix = []

for i in range(n):
    matrix.append(input().split())

for i in range(n):
    for j in range(m):
        print(matrix[~i][j], end=' ')
    print()
