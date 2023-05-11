# A. Матчи
#
#
# Манао работает на спортивном телевидении. Он долгое время наблюдал за футбольными матчами чемпионата одной страны и начал замечать разные закономерности. Например, у каждой команды есть две формы: домашняя и выездная. Когда команда проводит матч на своем стадионе, футболисты надевают домашнюю форму, а когда на чужом — выездную. Единственное исключение из этого правила — когда цвет домашней формы принимающей команды совпадает с цветом формы гостей. В таком случае домашняя команда облачается в свою выездную форму. Цвета домашней и выездной формы для каждой команды различны.
#
# В чемпионате страны участвует n команд и он состоит из n·(n - 1) матчей: каждая из команд принимает каждую другую команду на своем стадионе. Манао задумался, а сколько раз в течение одного чемпионата случится, что команда, играющая на своем стадионе, оденет выездную форму? Обратите внимание, что для подсчета этого количества порядок матчей не играет никакого значения.
#
# Вам даны цвета домашней и выездной формы каждой команды. Для удобства эти цвета пронумерованы целыми числами таким образом, что никакие два разных цвета не имеют одинаковый номер. Помогите Манао найти ответ на его вопрос.
#
# Входные данные
# В первой строке содержится целое число n (2 ≤ n ≤ 30). В каждой из следующих n строк записана пара разделенных одним пробелом различных целых чисел hi, ai (1 ≤ hi, ai ≤ 100) — номер цвета домашней и выездной форм i-ой команды соответственно.
#
# Выходные данные
# В единственной строке выведите количество матчей, в которых домашняя команда выступит в выездной форме.
#
# Разбор задачи Youtube Patreon Boosty
#
# Sample Input 1:
#
# 3
# 1 2
# 2 4
# 3 4
# Sample Output 1:
#
# 1
# Sample Input 2:
#
# 4
# 100 42
# 42 100
# 5 42
# 100 5
# Sample Output 2:
#
# 5
# Sample Input 3:
#
# 2
# 1 2
# 1 2
# Sample Output 3:
#
# 0

# n = int(input())
# number_of_color_changes = 0
# colors = []
# for _ in range(n):
#     h, a = map(int, input().split())
#     colors.append((h, a))
#
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if colors[i][0] == colors[j][1] or colors[i][1] == colors[j][0]:
#             number_of_color_changes += 1
#         if colors[i][0] == colors[j][1] and colors[i][1] == colors[j][0]:
#             number_of_color_changes += 1
# print(number_of_color_changes)

c = [input().split() for i in range(int(input()))]
print(sum([1 for i in c for j in c if i[1] == j[0]]))
