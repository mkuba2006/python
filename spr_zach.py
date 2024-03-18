import math
#plecak

# def stworz(itemy):
#     for i in itemy:
#         tab.append(
#         {
#             "nr": i["nr"],
#             "waga": i["waga"],
#             "wartosc": i["wartosc"],
#             "iloraz": round(i["wartosc"]/i["waga"],2),
#         })
    
    
# def sortuj(itemy):
#     for i in range(len(itemy)):
#         for j in range(len(itemy)-i-1):
#             if itemy[j]["iloraz"] < itemy[j+1]["iloraz"]:
#                 pom = itemy[j+1]
#                 itemy[j+1] = itemy[j]
#                 itemy[j] = pom
#     for i in itemy:
#         print(i)

# itemy = [
#     {"nr": 3, "waga": 5, "wartosc": 15},
#     {"nr": 1, "waga": 2, "wartosc": 3},
#     {"nr": 4, "waga":4, "wartosc": 11},
#     {"nr": 2, "waga": 3, "wartosc": 10},
#     {"nr": 5, "waga": 2, "wartosc": 4}
# ]

# tab=[]
# max_waga = 17
# max_wart = 0
# stworz(itemy)
# sortuj(tab) 

# for i in tab:
#     ile_wchodzi = math.floor(max_waga/i["waga"])
#     wchodząca_waga = ile_wchodzi * i["waga"]
#     max_wart += ile_wchodzi * i["iloraz"]
#     print("nr", i["nr"],"wchodzi",ile_wchodzi)
#     max_waga -= wchodząca_waga

# print("wartość plecaka:",max_wart)


#-----------------------------------------------------------------------------------------------------------

import random

dl = 4
t=[]


for z in range(dl):
    row=[]
    for a in range(dl):
        row.append(random.randint(1,9))
    row.append(0)
    t.append(row)
    print(row)
    row=[]
t.append([0,0,0,0,0])
print([0,0,0,0,0])

n = 2*dl-1
jakie=[t[0][0]]
r=0
c=0

for i in range(1,n):
    if t[r+1][c] > t[r][c+1]:
        jakie.append(t[r+1][c])
        r+=1
    else:
        jakie.append(t[r][c+1])
        c+=1
print(jakie)



#-----------------------------------------------------------------------------------------------------------

arr=[]
for _ in range(26):
    arr.append(random.randint)

