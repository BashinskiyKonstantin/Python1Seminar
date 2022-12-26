# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random
n = int(input("Введите количество элементов в списке: "))
list = []

for i in range(n):
    list.append(round((random.random() * 10), 2))

print(list)

max = round((list[0] - int(list[0])), 2)
min = round((list[1] - int(list[1])), 2)

for i in range(len(list)):
    list[i] = round((list[i] - int(list[i])), 2)
    if list[i] > max:
        max = list[i]
    if list[i] < min:
        min = list[i]

difference = round((max - min), 2)

print(
    f"Разница между максимальным и минимальным значением дробной части элементов:\n {max} - {min} = {difference}")
