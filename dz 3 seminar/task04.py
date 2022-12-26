# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input("Введите десятичное число: "))
result = 0
count = 1
while num > 0:
    result = int(result + num % 2 * count)
    num = int(num/2)
    count = count*10
print(f'Двоичный вид числа -> {result}')
