# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

print('Введите номер четверти')
n = int(input())


def CheckQuarter(n):
    if n == 1:
        print('X>0 и Y>0')
    elif n == 2:
        print('X<0 и Y>0')
    elif n == 3:
        print('X<0 и Y<0')
    elif n == 4:
        print('X>0 и Y<0')
    else:
        print('Такой четверти нет!')


CheckQuarter(n)
