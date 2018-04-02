a=[]
N=int(input('Введите количство строк и столбцов в матрице: '))
for i in range (N):
    a.append([])
    for m in range (N):
        k=int(input('Введите число a[%d][%d]: '%(i+1,m+1)))
        a[i].append(k)
print('\nИсходная матрица: ')
for i in range (N):
    print(a[i])
for j in range(N - 1, -1, -1):
    for i in a:
        print(i[j], end=" ")
    print()
