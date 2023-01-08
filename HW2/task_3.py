# 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

n = int(input('Введите число N: '))

current = 0
sequence = []

for i in range(1, n+1):
    current = (1 + 1 / i)**i
    sequence.append(current)

print(f'{sequence}')
print(sum(sequence))