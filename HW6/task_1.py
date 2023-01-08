# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# ' 'абвгд гдежз жзе абв ыопыпт' -> ' гдежз жзе ыопыпт'

# Вариант 1

# string = input("Введите текст через пробел: ")
# string = 'абвгд гдежз жзе абв ыопыпт'
# print(f'Текущий текст: {string}')
# find_string = "абв"
# string1 = [i for i in string.split() if find_string not in i]
# print(f'Новый текст: {" ".join(string1)}')

# Вариант 2

del_st = lambda x, y: " ".join([i for i in x.split() if y not in i])
print(del_st('абвгд гдежз жзе абв  ыопыпт', 'абв'))