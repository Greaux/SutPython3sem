massiv=list(map(str,input('text:').split()))
print (' '.join(map(str,sorted(massiv,key=lambda x: x[0]))))
