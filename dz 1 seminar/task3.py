# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def inputCoordinates(n):
    xy = ["X", "Y"]
    list = []
    for i in range(n):
        list.append(int(input(f"Введите значение {xy[i]}: ")))
    return list


def checkCoordinates(xy):
    if xy[0] != 0 and xy[1] != 0:
        if xy[0] > 0 and xy[1] > 0:
            quarter = 1
        elif xy[0] < 0 and xy[1] > 0:
            quarter = 2
        elif xy[0] < 0 and xy[1] < 0:
            quarter = 3
        elif xy[0] > 0 and xy[1] < 0:
            quarter = 4
        print(f"Точка ({xy[0]}, {xy[1]}) находится в {quarter} четверти плоскости")
    else:
        print(f"Значение координат X:({xy[0]}) и Y:({xy[1]}) не должны равняться нулю!")


checkCoordinates(inputCoordinates(2))
