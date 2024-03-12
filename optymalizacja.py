import random

dl =30
tablica=[]
nowa_tablica= []
for i in range(dl):
    tablica.append(random.randint(1,50))
tablica.sort()

max = 30
pierwsza = tablica[0]
for i in tablica:
    if pierwsza + i <= max:
        nowa_tablica.append(i)



def pary(tab): 
    print(nowa_tablica)
    print("dlugosc:",len(nowa_tablica))
    print("max", max)
    licznik = 0
    for i in range(len(tab)//2):
        print(tab[i],'-',tab[-i-1],'=', tab[i] +tab[-i-1])
        if tab[i] + tab[-i-1] <= max:
            licznik+=1
    print('licznik', licznik)

pary(nowa_tablica)