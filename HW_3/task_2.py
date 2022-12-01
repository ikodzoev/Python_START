"""
Задайте список целых чисел. Верните список с произведениями его парных элементов.
Парой считаются первый и последний элемент, второй и предпоследний и т.д.
Если элементов нечетное количество – центральный элемент умножается сам на себя.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>

Пример:
[2, 3, 4, 5, 6]
[12, 15, 16]

[2, 3, 5, 6]
[12, 15]
"""

print('Введите целые числа через пробел: ')
getlist = []
for element in input().split():
    getlist.append(int(element))


def mult_of_pair():
    if len(getlist) % 2 != 0:
        res = int(len(getlist) / 2) + 1
    else:
        res = int(len(getlist) / 2)

    mult = []
    for i in range(0, res):
        mult.append(getlist[i] * getlist[len(getlist) - 1 - i])
    return mult


print(mult_of_pair())
