"""
Задать натуральное число k.
Сформируйте многочлен (полином) степени k со случайными коэффициентами из промежутка от 0 до 100, включительно.
Многочлен вывести в консоль и записать в файл.

Ввод: значение типа <int>
Вывод: значение типа <str>, файл с одной строкой.

Пример:
2
2x^2 + 4x + 5 = 0
"""


from random import randint

k = int(input('Введите натуральное число k:'))

max_num = 100

ratio = [randint(0, max_num) for i in range(k)] + [randint(1, max_num)]
polynom = '+'.join([f'{(j, "")[j == 1]}x^{i}' for i, j in enumerate(ratio) if j][::-1])

polynom = polynom.replace('x^1+', 'x+')
polynom = polynom.replace('x^0', '')
polynom += ('', '1')[polynom[-1] == '+']
polynom = (polynom, polynom[:-2])[polynom[-2:] == '^1']

print(polynom, '= 0')

with open("polynom_res.txt", 'w') as data:
    data.write(str(polynom))
    data.write(str(' = 0'))
