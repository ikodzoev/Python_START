"""
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
По возможности реализуйте использования скобок, меняющих приоритет операций.

Ввод: значение типа <str>
Вывод: значение числового типа данных
"""
# Вариант 1:
import numexpr as calc
import re

operations = {"^": lambda a, b: str(float(a) ** float(b)),
              "/": lambda a, b: str(float(a) / float(b)),
              "*": lambda a, b: str(float(a) * float(b)),
              "+": lambda a, b: str(float(a) + float(b)),
              "-": lambda a, b: str(float(a) - float(b)),
              "%": lambda a, b: str(float(a) % float(b))}

priority_re = r"\((.+?)\)"
operations_re = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"


def arithmetics(exp: str) -> str:
    while match := re.search(priority_re, exp):
        exp: str = exp.replace(match.group(0), arithmetics(match.group(1)))

    for symbol, operation in operations.items():
        while match := re.search(operations_re.format(symbol), exp):
            exp: str = exp.replace(match.group(0), operation(*match.groups()))

    return exp


result = '(10 - 8) * (3 * (20 + 2)) / 4'
print(arithmetics(result))
# result = input('Введите арифметическое выражение: ')
# print(calc.evaluate(result))
# Вариант 2:
print(calc.evaluate('(10 - 8) * (3 * (20 + 2)) / 4'))
