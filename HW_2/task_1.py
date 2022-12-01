"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Ввод: значение типа <float>
Вывод: значение типа <int>

Примеры:
6782.0
23

0.56
11
"""

number = input('Введите число: ')
sum_digits = 0
for num in number:
    if num.isdigit():
        sum_digits += int(num)

print(sum_digits)
