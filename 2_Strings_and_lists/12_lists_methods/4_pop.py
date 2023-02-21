# Метод pop
# В вашем распоряжении список numbers.
# Ваша задача выполнить действия из списка строго в том же порядке, а именно:

# удалить элемент, стоящий на последней позиции;
# удалить элемент, стоящий на 0-й позиции;
# удалить элемент, стоящий на 12-й позиции;
# удалить элемент, стоящий на 7-й позиции;

#  В качестве ответа необходимо вывести на первой строке измененный список numbers,
#  а на второй - сумму значений удаленных элементов

numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]

print(numbers, sum([numbers.pop(idx) for idx in [-1, 0, 12, 7]]), sep='\n')
