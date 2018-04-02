from random import random

N = 5
M = 7

matrix = []
for i in range(N):
    a = [0] * M
    for j in range(M):
        a[j] = int(random() * 10)
        print('%3d' % a[j], end='')
    matrix.append(a)
    print()

summa = [0] * M
for j in range(M):
    for i in range(N):
        summa[j] += matrix[i][j]
    print('%3d' % summa[j], end='')
print('\n')

for j in range(M - 1):
    for i in range(M - j - 1):
        if summa[i] > summa[i + 1]:
            summa[i], summa[i + 1] = summa[i + 1], summa[i]
            for k in range(N):
                matrix[k][i], matrix[k][i + 1] = matrix[k][i + 1], matrix[k][i]

for i in matrix:
    for j in i:
        print('%3d' % j, end='')
    print()
for i in summa:
    print('%3d' % i, end='')
print()
