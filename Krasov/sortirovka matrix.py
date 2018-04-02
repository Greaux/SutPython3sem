import random

n = 6
a = [[random.randint(0,9)for j in range(n)]for i in range(n)]
print('Исходная матрица')
for i in range(n):
    print(a[i])
for i in range(n):
    for j in range(i):
        b = a[i][j]
        a[i][j] = a[j][i]
        a[j][i] = b
print('Перестановка')
for i in range(n):
    print(a[i])
flag= 1
while flag:
    flag = 0
    for i in range(n-1):
        if a[i]> a[i+1]:
            flag = 1
            b = a[i]
            a[i] = a[i+1]
            a[i+1] = b
print('Сортировка')
print(a)
