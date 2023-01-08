# 5. Реализуйте алгоритм перемешивания списка.

from random import randint
import random

lenght = 10
list = []

for i in range(lenght):
    current = int(randint(1,10))
    list.append(current)

print(f'Исходный список:     {list}')

random.shuffle(list)
print(f'Перемешанный список: {list}')