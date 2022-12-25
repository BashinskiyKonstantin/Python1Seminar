# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

print("Введите число")
a = abs(int(input()))
list = list(range(-a, a+1))
print(list)
listdata = []
with open('file.txt', 'w') as data:
    data.write(f'{a-1}\n')
    data.write(f'{a-2}\n')
    data.write(f'{a-3}\n')
    data.write(f'{a-3}')
file = 'file.txt'
data = open(file, 'r')
for line in data:
    listdata.append(int(line))
data.close()
result=1
for i in range(len(listdata)):
   listdata [i]=(list[listdata[i]])
   result = int (listdata[i] *result)
print (f'Произведение элементов на указанных позициях: {result}')
