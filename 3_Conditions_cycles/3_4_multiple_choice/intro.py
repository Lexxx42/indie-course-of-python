# Множественный выбор
# Сегодня мы с вами узнаем как программа сможет обрабатывать более чем 2 события
# без использования вложенного оператора if.
# Для этого нам понадобится инструкция elif.
# Она также как и else является необязательной частью оператора if.

# Само слово elif образовано от else if, что переводится как "иначе если".
# Напоминаю, что после  else условие никогда не ставится.
# А вот после elif вы обязательно должны поставить логическое выражение

# Синтаксически конструкция выглядит следующим образом:

# сначала записывается часть if с условным выражением, которое возвращает истину или ложь;
# затем может следовать одна или несколько необязательных частей elif
# (в других языках вы могли встречать else if);
# Завершается же запись этого составного оператора также необязательной частью else.
# Пример кода:

if 5 > 1:
    print(1)
    print(2)
elif 3 > 2:
    print(3)
    print(4)
elif 6 > 4:
    print(5)
    print(6)
elif 6 > 4:
    print(7)
    print(8)
else:
    print(9)
print('end')

# Из всех указанных блоков выполнится только 1,
# тот чье условие выполниться первым.
# Как только тело if или какого-нибудь elif выполняется,
# программа сразу же возвращается в основную ветку,
# а все нижеследующие elif, а также else пропускаются.



