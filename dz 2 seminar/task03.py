# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# Пример:

# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#         Сумма 9.06


n = int(input("Введите число "))
list = list(range(1, n+1))
sum = 0
for i in range(len(list)):
    list[i] = round((1+1/list[i])**list[i], 2)
    sum += list[i]
print(f'Последовательность:{list}\nСумма: {sum}')