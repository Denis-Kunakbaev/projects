from math import*
from random import*
num = randint(1,100)
print('Добро пожаловать в числовую угадайку','Введите число от 1 до 100:', sep = '\n')

def is_valid(txt):
    return txt.isdigit() and 0 < int(txt) < 101

def is_ask():
    while True:
        n = input()
        if is_valid(n):
            return int(n)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')

def is_number():
    while True:
        n = is_ask()
        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else: 
            print('Вы угадали, поздравляем!')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break

is_number()