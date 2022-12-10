"""
Реализуйте код игры.
Правила игры: на столе лежит N количество конфет. Играют два игрока, делая ход друг после друга.
Первый ход определяется жеребьёвкой, то есть случаен. За один ход можно забрать не более чем k конфет.
Не брать конфеты НЕЛЬЗЯ. Побеждает тот, кто сделал последний ход, то есть забрал со стола остатки конфет.
Он забирает также все конфеты оппонента.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего оппонента?

a) Добавьте игру против бота
b) Подумайте, как наделить бота простейшим "интеллектом"
"""

from random import randint


def in_data(name):

    total = int(input(f'{name}, введите количество конфет, которое возьмете от 1 до {take_once}: '))
    while total < 1 or total > take_once:
        total = int(input(f'{name}, введите корректное количество конфет: '))
    return total


def print_data(name, k, counter, value):
    print(f'Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе конфет: {value}')


player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')
value = int(input('Введите количество конфет на столе: '))
flag = randint(0, 2)
if flag:
    print(f'Первый ходит {player1}')
else:
    print(f'Первый ходит {player2}')

counter1 = 0
counter2 = 0
take_once = int(input('Введите количество конфет, которое можно взять за один ход: '))
while value > take_once:
    if flag:
        k = in_data(player1)
        counter1 += k
        value -= k
        flag = False
        print_data(player1, k, counter1, value)
    else:
        k = in_data(player2)
        counter2 += k
        value -= k
        flag = True
        print_data(player2, k, counter2, value)

if flag:
    print(f'Выиграл {player1}, теперь у него все конфеты.')
else:
    print(f'Выиграл {player2}, теперь у него все конфеты.')
