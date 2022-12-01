"""
Напишите программу, которая принимает на вход натуральное число N и выдает список факториалов по основаниям от 1 до N

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
4
[1, 2, 6, 24]
"""

N = int(input('Введите число: '))


def getlist():
    total = 1
    current = 1
    while True:
        total = total * current
        yield total
        current = current + 1


f = getlist()
print([next(f) for i in range(N)])
