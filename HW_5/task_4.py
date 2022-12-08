"""
Реализуйте RLE алгоритм шифрования строки: замените повторяющиеся символы строки на один символ и число его повторов.
На первом месте идет количество повторов, на втором сам символ.
Восстановите строку после шифрования.

Ввод: значения типа <str>, можно получить из файла.
Вывод: значение типа <str>, можно записать в файл.

Примеры:
ыыыыыррррр   аааааагггггггг
5ы5р3 6а8г
"""
text = input('Введите текст: ')


def encoding(seq):
    count = 1
    res = []
    for x, item in enumerate(seq):
        if x == 0:
            continue
        elif item == seq[x - 1]:
            count += 1
        else:
            res.append((seq[x - 1], count))
            count = 1
    res.append((seq[len(seq) - 1], count))
    return res


def decoding(seq):
    res = []
    for item in seq:
        res.append(item[0] * item[1])
    return ''.join(res)


def cod_format(seq):
    res = []
    for item in seq:
        if item[1] == 1:
            res.append(item[0])
        else:
            res.append(str(item[1]) + item[0])
    return ''.join(res)


print('Изначальный текст: ' + text)
print(f'Зашифрованный текст: {cod_format(encoding(text))}')
print(f'Дешифрованный текст: {decoding(encoding(text))}')
