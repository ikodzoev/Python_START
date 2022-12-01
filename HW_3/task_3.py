"""
Задайте список из вещественных чисел, округленных до сотых.
Найдите разницу между максимальным и минимальным значением дробной части элементов.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <float>

Пример:
[1.1, 1.2, 3.1, 5, 10.01]
2.0
"""
print('Введите вещественные числа через запятую: ')
getlist = []
for element in input().split(','):
    getlist.append(float(element))


# getlist = [1.1, 1.2, 3.1, 5, 10.01]


def diff():
    max_fract = 0
    min_fract = 1
    for i in getlist:
        buf = round(i % 1, 2)
        if buf > max_fract:
            max_fract = buf
        elif buf < min_fract:
            min_fract = buf
    res = (round((max_fract - min_fract), 2) * 10)
    # print(f"max {max_fract}, min {min_fract}")
    return res


print(diff())
