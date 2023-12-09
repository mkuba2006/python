n= int(input("wczytaj :"))


def silnia():
    silnia=1
    for i in range(1,n+1):
        silnia*=i
    print(silnia)
    
silnia()