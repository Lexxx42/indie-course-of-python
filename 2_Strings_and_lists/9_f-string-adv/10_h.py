# Вам необходимо подправить код ниже так, чтобы он выравнивал

# первый print по центру
# второй print по правому краю
# третий print по левому краю
# Количество знаков для выравнивания 20 символов, знак разделителя - &

# Sample Input 1:

# hello
# Sample Output 1:

# |&&&&&&&hello&&&&&&&&|
# |&&&&&&&&&&&&&&&hello|
# |hello&&&&&&&&&&&&&&&|

print(f'|{(s := input()):&^20s}|\n|{s:&>20s}|\n|{s:&<20s}|')
