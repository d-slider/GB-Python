
# 2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [1,2,3]
# * 144 -> [2,3]

a = int(input("Введите натуральное число: "))
i = 2 
list = []

print(f'Простые множители числа {a}: ', end='')
while i <= a:
    if a % i == 0:
        list.append(i)
        a //= i
        i = 2
    else:
        i += 1

print(list)

