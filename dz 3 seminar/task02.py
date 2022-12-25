# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
list = list(range(1, 5))
listresult = []
random.shuffle(list)
if int(len(list) % 2 == 1):
    for i in range(int(((len(list))+1)/2)):
        listresult.append(list[i]*list[len(list)-1-i])
else:
    for i in range(int((len(list))/2)):
        listresult.append(list[i]*list[len(list)-1-i])

print(f"Массив: {list}")
print(f"Результат: {listresult}")
