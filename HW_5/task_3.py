"""
Напишите игру "Крестики-нолики".
"""


def main():
    # Запуск функций:
    start_info()
    board = get_grid()
    print_tab(board)
    symbol_1, symbol_2 = sym()
    full_fill(board, symbol_1, symbol_2)


def start_info():
    # Правила игры:
    print('Добро пожаловать в игру Крестики и нолики!')
    print('\n')
    print('Правила игры: '
          'Игроки по очереди ставят на свободные клетки поля 3×3 знаки X ("крестик") или 0 ("нолик") ' '\n'
          'Первый игрок, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, побеждает в игре.')
    print('\n')
    input('Нажмите enter для продолжения.')
    print('\n')


def get_grid():
    # Создание игрового поля:
    print('Это игровое поле: ')
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    return board


def sym():
    # Выбор игрового знака: крестик или нолик:
    symbol_1 = input('Игрок 1, выберите, чем играть: X или O? ')
    if symbol_1 == 'X':
        symbol_2 = 'O'
        print('Игрок 2 играет 0 (ноликами). ')
    else:
        symbol_2 = 'X'
        print('Игрок 2 играет X (крестиками). ')
    input('Нажмите enter для продолжения.')
    print('\n')
    return symbol_1, symbol_2


def start_game(board, symbol_1, symbol_2, count):
    # Старт игры.

    # очерёдность хода:
    player = None
    if count % 2 == 0:
        player = symbol_1
    elif count % 2 == 1:
        player = symbol_2
    print('Игрок ' + player + ', теперь ваш ход. ')
    row = int(input('Выберите строку:'
                    '[верхняя: введите 0, средняя: нажмите 1, нижняя: введите 2]:'))
    column = int(input('Выберите столбец:'
                       '[левый: введите 0, средний: нажмите 1, правый: введите 2]'))

    # проверка на выход ячейки за рамки игровой таблицы:
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        out_game()
        row = int(input('Выберите строку [верхнюю:'
                        '[введите 0, среднюю: введите 1, нижнюю: введите 2]:'))
        column = int(input('Выберите столбец:'
                           '[левый: введите 0, средний: нажмите 1, правый: введите 2]'))

        # проверка на заполненность клетки:
    while (board[row][column] == symbol_1) or (board[row][column] == symbol_2):
        illegal()
        row = int(input('Выберите строку [верхнюю:'
                        '[введите 0, среднюю: введите 1, нижнюю: введите 2]:'))
        column = int(input('Выберите столбец:'
                           '[левый: введите 0, средний: нажмите 1, правый: введите 2]'))

        # определение местоположения знака игрока на игровом поле
    if player == symbol_1:
        board[row][column] = symbol_1

    else:
        board[row][column] = symbol_2

    return board


def full_fill(board, symbol_1, symbol_2):
    count = 1
    winner = True
    # Проверка заполненности игровой таблицы
    while count < 10 and winner is True:
        start_game(board, symbol_1, symbol_2, count)
        print_tab(board)

        if count == 9:
            print('Все клетки заполнены. Игра окончена.')
            if winner:
                print('Ничья победила. ')

        # проверка наличия победителя:
        winner = is_winner(board, symbol_1, symbol_2)
        count += 1
    if not winner:
        print('Игра окончена.')


def out_game():
    # Предупреждение о выходе за пределы игровой таблицы:
    print('Вы вышли за пределы поля. Укажите другую клетку. ')


def print_tab(board):
    # Вывод в консоли игровой таблицы:
    rows = len(board)
    print('---+---+---')
    for r in range(rows):
        print(board[r][0], ' |', board[r][1], '|', board[r][2])
        print('---+---+---')
    return board


def is_winner(board, symbol_1, symbol_2):
    # Проверка, выигрывает ли победитель
    winner = True
    # проверка строк:
    for row in range(0, 3):
        if board[row][0] == board[row][1] == board[row][2] == symbol_1:
            winner = False
            print('Игрок ' + symbol_1 + ', выиграл!')

        elif board[row][0] == board[row][1] == board[row][2] == symbol_2:
            winner = False
            print('Игрок ' + symbol_2 + ', выиграл!')

    # проверка столбцов:
    for col in range(0, 3):
        if board[0][col] == board[1][col] == board[2][col] == symbol_1:
            winner = False
            print('Игрок ' + symbol_1 + ', выиграл!')
        elif board[0][col] == board[1][col] == board[2][col] == symbol_2:
            winner = False
            print('Игрок ' + symbol_2 + ', выиграл!')

    # проверка диагоналей:
    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = False
        print('Игрок ' + symbol_1 + ', выиграл!')

    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = False
        print('Игрок ' + symbol_2 + ', выиграл!')

    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = False
        print('Игрок ' + symbol_1 + ', выиграл!')

    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print('Игрок ' + symbol_2 + ', выиграл!')

    return winner


def illegal():
    print('Выбранная клетка уже заполнена. Выберите другую.')


def report(count, winner, symbol_1, symbol_2):

    # сводка результатов игры
    print('\n')
    input('Нажмите enter, чтобы просмотреть результат игры. ')
    if winner is False and (count % 2 == 1):
        print('Победитель : Игрок ' + symbol_1 + '.')
    elif winner is False and (count % 2 == 0):
        print('Победитель : Игрок ' + symbol_2 + '.')
    else:
        print('Ничья. ')


# Вызов главной функции:
main()
