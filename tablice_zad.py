import random

dł = 4
tablica = []
tablica_cols = []
def stworz_tablice(dł):
    for i in range(dł):
        row = []
        for j in range(dł):
            liczba = random.randint(0, 9)
            row.append(liczba)
        tablica.append(row)
        # print(row)
        row = []
    
def sortuj_tablice():
    for i in range(len(tablica)):
        tablica[i] = sorted(tablica[i])

def policz_sume_rows():
    for i in range(len(tablica)):
        suma = 0
        row = tablica[i]
        for j in range(len(row)):
            suma += row[j]
        print(row,"=",suma)
    print('-------')
    
    
def stworz_cols():  
    tablica_cols = list(zip(*tablica))
    print(tablica_cols)
    
    
    
    
    
    
    
stworz_tablice(dł)
sortuj_tablice()
policz_sume_rows()
stworz_cols()
