"""
Задайте список целых чисел. Найдите сумму элементов списка, имеющих нечетные индексы.

Ввод: значение типа <list> (либо значение типа <int> – размерность списка)
Вывод: значение типа <int>

Примеры:
[2, 3, 5, 9, 3]
12

[5, 1, 5, 2, 7, 11]
14
"""

getlist = []
print('Введите целые числа через пробел: ')
for element in input().split():
    getlist.append(int(element))
# print(getlist)
sum_odd = sum(getlist[1::2])
print(sum_odd)
# print(type(sum_odd))
