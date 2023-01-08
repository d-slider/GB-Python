#  Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

n = [1,2,3,33,45,22,11,2,3,11,4,3,4,66,7] 
uniq = []
sort = []

for i in n:
    if i not in uniq:
        uniq.append(i)

print('orig:', n)
print('uniq:',uniq)

while len(uniq) != 0:
    sort.append(min(uniq))
    uniq.remove(min(uniq))

print('sort:',sort)