"""
Напишите программу, удаляющую из текста все слова, в которых присутствуют буквы «а», «б» и «в».

Ввод: значение типа <str>
Вывод: значение типа <str>
"""
s = input('Введите любой текст: ')
get_move = 'абв'
# # Удаляет все слова, в которых есть буквы «а», «б» и «в» (любая из букв):
# print(' ' .join(list(filter(lambda str_: all(i not in str_.lower() for i in get_move), s.split()))))
# # Удаляет все слова, в которых ОДНОВРЕМЕННО присутствуют буквы «а», «б» и «в» в любом порядке:
print(' ' .join(list(filter(lambda str_: not all(i in str_.lower() for i in get_move), s.split()))))
