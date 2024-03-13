import math

def stworz(itemy):
    for item in itemy:
        iloraz = round(item["wartosc"] / item["waga"],2)
        itema = {
            "nr": item["nr"],
            "waga": item["waga"],
            "wartosc": item["wartosc"],
            "iloraz": iloraz,
        }
        tab.append(itema)
        print(itema)
        
def sortuj(itemy):
    for i in range(len(itemy)):
        for j in range(len(itemy)-i-1):
            if itemy[j]["iloraz"] < itemy[j + 1]["iloraz"]:
                pom = itemy[j+1]
                itemy[j + 1] = itemy[j]
                itemy[j] = pom
    print('----Nowa Tablica-----')
    for i in tab:
        print(i)

# -------------------------------------------------------------- #

itemy = [
    {"nr": 3, "waga": 5, "wartosc": 15},
    {"nr": 1, "waga": 2, "wartosc": 3},
    {"nr": 4, "waga":4, "wartosc": 11},
    {"nr": 2, "waga": 3, "wartosc": 10},
    {"nr": 5, "waga": 2, "wartosc": 4}
]



tab= []
max_waga = 17
max_wart = 0
stworz(itemy)
sortuj(tab)

for item in tab:
    ile_wejdzie = math.floor(max_waga / item["waga"])
    waga_wchodzacych = ile_wejdzie * math.floor(item["waga"])
    max_waga -= waga_wchodzacych
    max_wart += ile_wejdzie * item["wartosc"]
    print("nr", item["nr"],"o wartosci",item["iloraz"], "wejdzie", ile_wejdzie)
print(max_wart)


