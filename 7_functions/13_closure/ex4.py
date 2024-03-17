# Ваша задача создать функцию-замыкание create_dict, она должна сохранять в себе все значения, которые ей будут переданы причем в виде словаря. Ключами данного словаря должны быть натуральные числа, равные номеру вызова данной функции. Посмотрите пример ниже:
#
# f_1 = create_dict()
# print(f_1('hello')) # f_1 возвращает {1: 'hello'}
# print(f_1(100)) # f_1 возвращает {1: 'hello', 2: 100}
# print(f_1([1, 2, 3])) # f_1 возвращает {1: 'hello', 2: 100, 3: [1, 2, 3]}
#
# f_2 = create_dict() # создаем новое замыкание в f_2
# print(f_2('PoweR')) # f_2 возвращает {1: 'PoweR'}
# Вызывая первый раз f_1 мы создали пару 1: 'hello', вызывая второй раз добавилась пара 2: 100. и т.д.
#
# При каждом вызове должен возвращаться словарь, хранящийся в замыкании
#
# Необходимо только определить функцию-замыкание create_dict, остальное мы сделаем за вас

def create_dict(val=None):
    count = 1
    result = {}

    def inner(a):
        nonlocal count
        result[count] = a
        count += 1
        return result

    return inner


f_1 = create_dict()
print(f_1('hello'))  # f_1 возвращает {1: 'hello'}
print(f_1(100))  # f_1 возвращает {1: 'hello', 2: 100}
print(f_1([1, 2, 3]))  # f_1 возвращает {1: 'hello', 2: 100, 3: [1, 2, 3]}
