# Напишите программу, которая сначала считывает три фразы по очереди,
# а потом воспроизводит их в обратной последовательности, каждую на отдельной строчке.

# Sample Input:

# Привет!
# Артем
# Как дела?
# Sample Output:

# Как дела?
# Артем
# Привет!

# print(*[input() for _ in range(3)][::-1], sep='\n')
[print(i) for i in [input() for _ in range(3)][::-1]]
