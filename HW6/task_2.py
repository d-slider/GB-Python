# 2. Напишите программу, которая на вход принимает 5 чисел 
# и находит максимальное из них

# Вариант 1
# max = int(input())
# for i in range(4):
#     b = int(input())
#     if b > max:
#       max = b
# print(max) 

# Вариант 2

a = list(map(int, '1 2 3 6 4'.split()))  
print(max(a))