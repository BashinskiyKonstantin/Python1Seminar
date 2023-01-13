# 27. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

a = input()
list_num = a.split()
list_num = list(map(int,list_num))
print(max(list_num),min(list_num))