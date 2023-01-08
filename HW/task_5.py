# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print(f'Введите координаты точки А:')
ax = float(input('x: '))
ay = float(input('y: '))

print(f'Введите координаты точки B:')
bx = float(input('x: '))
by = float(input('y: '))

print(f'Расстояние между точками ({ax};{ay}) ; ({bx};{by}) -> {round(pow((bx - ax)**2 + (by - ay)**2,0.5),2)}')
