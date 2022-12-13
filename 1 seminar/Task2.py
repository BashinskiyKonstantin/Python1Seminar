# 2.Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# a = int(input())
# max = a
# for i in range(5):
#   a = int(input())
#   if a>max:
#     max = a
# print(max)

# a = input()
# list_num = a.split(",")
# print(max(list_num))

a = input()
list_num = list(map(int, a.split(" ")))
print(list_num)
