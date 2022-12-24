# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def inputCoordinates(n):
    xy1xy2 = ["X1", "Y1", "X2", "Y2"]
    list = []
    for i in range(n):
        list.append(int(input(f"Введите координаты точки {xy1xy2[i]}: ")))
    return list

def CoordinateDistance(list):
    result = ((list[2] - list[0]) ** 2 + (list[3] - list[1]) ** 2) ** 0.5
    return result


print(f"Расстояние между точками: {format(CoordinateDistance(inputCoordinates(4)), '.2f')}")