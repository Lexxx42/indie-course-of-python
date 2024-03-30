# Декоратор-запоминатор
# Давайте вспомним рекурсивную функцию Фибоначчи
#
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
# Проблема работы этой функции в том, что она постоянно будет вызывать одни и те же значения, что будет сказываться на скорости работы. Если вызвать ее от десяти
#
# print(fibonacci(10))
# то она быстро завершит работу и вернет результат. Но попробуйте дождаться завершения если вызовете от сорока
#
# print(fibonacci(40))
# Дождаться пока функция найдет сотое число Фибоначчи будет нереально. Но мы можем придумать декоратор, который будет запоминать в себе аргументы функции и возвращаемые значения. Для этого нужно воспользоваться мемоизацией
#
# Мемоизация — это метод сохранения результатов ресурсоемких вызовов функций и возврата ранее вычисленного (кэшированного) результата при повторении одних и тех же входных данных. Это может значительно повысить производительность рекурсивных функций, которые в противном случае могут привести к многократному выполнению одних и тех же вычислений.
#
# В этом задании вам нужно определить декоратор memoize, который принимает функцию в качестве аргумента и возвращает функцию-оболочку. Функция-оболочка проверяет, были ли входные данные для функции просмотрены ранее и сохранены ли они в кеше. Если это так, функция просто возвращает кэшированный результат. Если нет, она вызывает исходную функцию и сохраняет результат в кеше для использования в будущем. Кеш представляет собой хранилище ранее вычиленных значений, в нашем случае можно использовать словарь
#
# Затем мы применяем этот декоратор к рекурсивной функции fibonacci. Когда функция fibonacci вызывается с определенным входным значением, логика мемоизации проверяет, был ли результат уже рассчитан и сохранен в кеше. Если был, кэшированный результат возвращается немедленно. Если нет, то будет вызвана функция fibonacci для вычисления результата, и результат будет сохранен в кеше для использования в будущем.
#
# Ваша задача реализовать декоратор memoize, который помимо выше описанного еще и должен сохранить первоначальное имя декорируемой функцию и ее строку документации
#
# Sample Input:
#
# Sample Output:
#
# Good


# Напишите определение декоратора memoize
def memoize(func):
    d = {}

    def inner(n):
        inner.__doc__ = func.__doc__
        inner.__name__ = func.__name__

        if n not in d:
            d[n] = func(n)

        return d[n]

    return inner


# Код ниже не удаляйте, он нужен для проверки


@memoize
def fibonacci(n):
    """
    Возвращает n-ое число Фибоначчи
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


assert fibonacci(50) == 12586269025
assert fibonacci(60) == 1548008755920
assert fibonacci(70) == 190392490709135
assert fibonacci(80) == 23416728348467685
assert fibonacci(90) == 2880067194370816120
assert fibonacci(100) == 354224848179261915075
assert fibonacci.__name__ == 'fibonacci'
assert fibonacci.__doc__.strip() == 'Возвращает n-ое число Фибоначчи'
print('Good')
