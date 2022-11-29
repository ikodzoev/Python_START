"""
Задайте список из N элементов, заполненный целыми числами из промежутка [-N, N].
Найдите произведение элементов на индексах, хранящихся в файле indexes.txt (в одной строке один индекс).
Решение должно работать при любом натуральном N.

Ввод: значение типа <int>
Вывод: значение типа <int>
"""
import random

rnd = random.Random()
getlist = []
n = int(input("Введите число N: "))
for i in range(n):
    getlist.append(rnd.randint(-n, n))
print(getlist)

output = 1
with open('indexes.txt', 'r') as data:
    for line in data:
        position = int(line)
        if n > position >= -n:
            output *= getlist[position]
print(output)
