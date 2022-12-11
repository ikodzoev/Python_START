"""
Даны файлы, в каждом из которых находится запись многочлена.
Найти сумму многочленов из файлов, ввести в консоль и записать в файл.
Входными данными для этой задачи являются выходные данные их предыдущей.

Ввод: значения типа <str>, полученные из файлов.
Вывод: значение типа <str>, файл с одной строкой.

Примеры:
9x^5+7x^4+7x^3+9x^2+6x+17=0
3x^2+2x+1=0
9x^5+7x^4+7x^3+12x^2+8x+18=0
"""

with open('polynom_res1.txt', 'r') as data:
    polynom_res1 = data.read()
with open('polynom_res2.txt', 'r') as data:
    polynom_res2 = data.read()

file_1 = open('polynom_res1.txt', 'r')
file_2 = open('polynom_res2.txt', 'r')
sum_poly = open('polynom_res_sum.txt', 'w')
file1 = file_1.readline()
file2 = file_2.readline()
for i in range(len(file1)):
    if file1[i - 1] != '^':
        if file1[i].isnumeric():
            sum_poly.write(str(int(file1[i]) + int(file2[i])))
        else:
            sum_poly.write(str(file1[i]))
    else:
        sum_poly.write(str(file1[i]))

sum_poly = open('polynom_res_sum.txt', 'r')

with open('polynom_res_sum.txt', 'r') as data:
    polynom_res_sum = data.read()
print(polynom_res_sum)
