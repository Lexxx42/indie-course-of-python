# Напишите код для преобразования списка из целых чисел произвольной длины в словарь,
# вложенность которого зависит от длины списка.

# Например, если перед вами был бы такой список

# [100, 55, 77, 55, 89]
# то он должен превратиться в такой словарь

# {100: {55: {77: {55: 89}}}}

# На вход программе поступают числа для списка в одну строку, гарантируется,
# что в списке будет как минимум два элемента.

# Ваша задача вывести полученный словарь

# Любую задачу можно сделать несколькими способами, эта задача не исключение
# Когда вы изучите рекурсию, советую вернуться к этой задаче полезно и попробовать решить рекурсивно

sequence = map(int, input().split()[::-1])
nested_dict = next(sequence)
print([nested_dict := {key: nested_dict} for key in sequence][-1])
