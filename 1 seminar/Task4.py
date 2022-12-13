# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

#     *Примеры:*

#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

print("Введите число")
a = float(input())
a = int(a * 10)
a = a % 10
if a > 0:
    print(a)
else:
    print("Числа нет")

# n = input()
# list_num = n.split(".")
# if len(list_num) > 1:
#     print(list_num)
#     print(list_num[1][0])
