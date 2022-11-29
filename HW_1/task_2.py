"""
Докажите, что выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно для всех значений предикат.

Вывод: единственное значение типа bool (True либо False)
"""
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(not (x or y or z) == (not x and not y and not z))
#             print(x, y, z)

x = int(input('Введите значение X: '))
y = int(input('Введите значение Y: '))
z = int(input('Введите значение Z: '))


def check_val():
    if not (x or y or z) == (not x and not y and not z):
        return True
    else:
        return False


print(check_val())
