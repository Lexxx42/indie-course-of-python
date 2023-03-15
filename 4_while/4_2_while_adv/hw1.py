# Пользователь вводит целые числа по одному в строке,
# последовательность оканчивается числом 0.
# Все, что вводится после 0 не относится к последовательности.
# Напишите программу, которая выводит сумму всех членов данной последовательности.

# 🚀 Подсказка
# Sample Input 1:

# 1
# 2
# 3
# 0
# 5
# 6
# Sample Output 1:

# 6
# Sample Input 2:

# -5
# 10
# 0
# 1
# 2
# 3
# Sample Output 2:

# 5
# Sample Input 3:

# -1
# -2
# -3
# 0
# Sample Output 3:

# -6
# Sample Input 4:

# 4
# 0
# 6
# Sample Output 4:

# 4

numbers = []
while (num := int(input())) != 0:
    numbers.append(num)
print(sum(numbers))
