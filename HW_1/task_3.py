"""
Напишите программу, принимающую на вход координаты точки (X и Y) и выдающую номер четверти плоскости,
в которой находится эта точка (или на какой оси она находится).

Ввод: два значения типа <int>
Вывод: значение типа <int> либо значение типа <str>

Пример:

34
-30
4

2
4
1

-34
0
Точка на отрицательной части оси абсцисс
"""
x = int(input('Введите координату X: '))
y = int(input('Введите координату Y: '))

if x > 0 < y:
    print('Точка находится в первой четверти')
elif x < 0 < y:
    print('Точка находится во второй четверти')
elif x < 0 > y:
    print('Точка находится в третьей четверти')
elif x > 0 > y:
    print('Точка находится в четвёртой четверти')
elif x == 0 > y:
    print('Точка на отрицательной части оси ординат')
elif x == 0 < y:
    print('Точка на положительной части оси ординат')
elif x > 0 == y:
    print('Точка на положительной части оси абсцисс')
elif x < 0 == y:
    print('Точка на отрицательной части оси абсцисс')
else:
    print('Точка находится в начале координат')
