# 13. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
# Пример:
# Строка - "dabccabccabcc"
# Подстрока - "ab"
# Количество вхождений - 3

line = input("Введите строку: ")
sub_line = input("Введите подстроку: ")

count = 0

for i in range(0, len(line)-len(sub_line)+1):
    if line[i:i+len(sub_line)] == sub_line:
        count += 1
print(count)
# text = input('Введите строку: ')
# subtext = input('Введите подстроку: ')ab

# print(text.count(subtext))
