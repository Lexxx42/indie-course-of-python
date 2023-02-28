# Даны три натуральных числа a, b, c записанные в отдельных строках.
# Ваша задача определить, существует ли треугольник с такими сторонами.

# Для этого вспоминаем теорему о существовании треугольника.
# Она утверждает, что треугольник существует,
# если сумма любых двух сторон больше оставшейся третьей.

# Выведите строку YES, если условие теоремы выполняется, иначе выведите строку NO.

# 🚀Если не справляетесь, здесь подсказка🚀
# Sample Input 1:

# 3
# 4
# 5
# Sample Output 1:

# YES
# Sample Input 2:

# 2
# 7
# 2
# Sample Output 2:

# NO

print('YES' if (b := (max(a := [int(input()) for _ in range(3)]))) < sum(a) - b else 'NO')
