import random
dl= 4
tab=[]


for i in range(dl):
    row =[]
    for j in range(dl):
        row.append(random.randint(1,9))
    row.append(0)
    tab.append(row)
    print(row)
    row=[]
tab.append([0,0,0,0,0])
print([0,0,0,0,0])


n = 2*dl-1
r=0
c=0
pierwsza = tab[0][0]
jakie = []
suma = tab[0][0]

for i in range(1,n):
    if tab[r+1][c] > tab[r][c+1]:
        jakie.append(tab[r+1][c])
        r+=1
    else:
        jakie.append(tab[r][c+1])
        c+=1
print(jakie)
for i in jakie:
    suma += i
print(suma)