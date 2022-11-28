"""
Задайте список из N элементов, заполненный целыми числами из промежутка [-N, N].
Найдите произведение элементов на индексах, хранящихся в файле indexes.txt (в одной строке один индекс).
Решение должно работать при любом натуральном N.

Ввод: значение типа <int>
Вывод: значение типа <int>
"""
from random import randint


def getlist():
    i_list = []
    for i in range(n):
        i_list.append(randint(-n, n))
    return i_list


n = 50
numbers = getlist()
print(numbers)
x = open('indexes.txt', 'r')
output = numbers[int(x.readline())] * numbers[int(x.readline(2))]
print(output)
