# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def inputCoordinates(n):
    xyz = ["X", "Y", "Z"]
    list = []
    for i in range(n):
        list.append(input(f"Введите значение {xyz[i]}: "))
    return list


def checkPredicate(list):
    oneCheking = not (list[0] or list[1] or list[2])
    secondCheking = not list[0] and not list[1] and not list[2]
    result = oneCheking == secondCheking
    return result


if checkPredicate(inputCoordinates(3)):
    print("Утверждение истинно!")
else:
    print("Утверждение ложно!")
