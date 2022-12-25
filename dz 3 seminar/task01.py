# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random
list = list(range(5))
random.shuffle(list)
listInSum = list[1:len(list):2]
sum = 0
for i in range(len(listInSum)):
    sum = listInSum[i] + sum
print(list)
print(f"Сумма элементов на нечетных позициях равна: {sum}")

