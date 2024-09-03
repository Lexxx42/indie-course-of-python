"""
Необходимо дописать функцию convert, которая перевернет слово
и вернет перевернутое слово, является ли слово палиндромом, и если является - дполнительно вернет 1 и последнюю букву,
а если не является, то количество символов между 1 и последним символом

Необходимо дополнительно указать у функции тип возвращаемого значения
"""


# 1) функция convert
def convert(word: str) -> str | list[str | bool | int]:
    result: list[str | bool | int] = []

    if not isinstance(word, str):
        return 'TypeError'

    if len(word) <= 1:
        return 'ValueError'

    result.append(word[::-1])

    if word.upper() == word[::-1].upper():
        result.append(True)
        result.append(f'{word[0]}{word[-1]}')

    else:
        result.append(False)
        result.append(len(word[1:-1]))

    return result


# 2) тесты
print(convert('Шалаш'))

assert convert('самсон') == ['носмас', False, 4]
assert convert('шалаш') == ['шалаш', True, 'шш']
assert convert('Шалаш') == ['шалаШ', True, 'Шш']
assert convert(-3) == 'TypeError'
assert convert('') == 'ValueError'
