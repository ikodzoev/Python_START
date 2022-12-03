"""
Выведите список простых множителей натурального числа N.

Ввод: значение типа <int>
Вывод: значение типа <list>

Примеры:
20
[2, 2, 5]

38
[2, 19]
"""
number = int(input("Введите натуральное число: "))
prev = 2
getlist = []
while prev <= number:
    if number % prev == 0:
        getlist.append(prev)
        number //= prev
    else:
        prev += 1
print(getlist)
