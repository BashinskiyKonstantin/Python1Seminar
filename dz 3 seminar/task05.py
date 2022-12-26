# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


num = int(input("Задайте число: "))


def postive(num):
    list = [1, 1]
    for i in range(num-2):
        list.append(list[-2]+list[-1])
    return list


def negative(num):
    list = [0, 1]
    for i in range(num-1):
        list.append(list[-2]-list[-1])
    return list


negativeFib = negative(num)
negativeFib.reverse()

print(f"Для {num} список будет выглядеть так:\n {negativeFib + postive(num)}")
