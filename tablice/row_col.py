import random
l=4
tabela=[]

for i in range(l):
    row = []
    for i in range(l):
        row.append(random.randint(0,1))
    tabela.append(row)
    print(row)
    
cols = list(zip(*tabela))
print(cols)
suma = 0
for i in cols:
    for j in i:
        suma += j
print(suma)