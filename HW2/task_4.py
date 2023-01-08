# 4'. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.tfilet в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2
# Позиции: 0,1 -> 2



def createList(n):
    list = []
    k = -n
    
    for i in range(2*n+1):
        list.append(k)
        k+=1
    return list

n = int(input('Введите число N: '))
list = createList(n)
print(list)

file = open('file.txt','r')
result = list[int(file.readline())] * list[int(file.readline(2))]

print(result)
file.close()