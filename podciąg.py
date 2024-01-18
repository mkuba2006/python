


# zad 1
# arr = [2, 5, 8, 12, 15, 18, 21, 4, 7, 10, 13, 16, 19, 22, 1, 3, 16, 9, 16, 14, 17, 20, 23, 25, 24, 8, 5, 2, 1, 10, 1, 2, 3, 4, 5, 6, 7, 8]
# podciagi=[]
# akt=[arr[0]]
# for i in range(1,len(arr)):
#     if arr[i] < arr[i-1]:
#         akt.append(arr[i])
#     else:
#         podciagi.append(akt)
#         akt = [arr[i]]
    
# posortowane = sorted(podciagi)
# print(posortowane[-1])



# zad 2 

# arr = [2, 5, 8, 12, 15, 18, 21, 4, 7, 10, 13, 16, 19, 22, 1, 3, 16, 9, 16, 14, 17, 20, 23, 25, 24, 8, 5, 2, 1, 10, 1, 2, 3, 4, 5, 6, 7]
# podciagi=[]
# akt=[arr[0]]
# for i in range(1,len(arr)):
#     if arr[i] > arr[i-1]:
#         akt.append(arr[i])
#     else:
#         podciagi.append(akt)
#         akt = [arr[i]]
# podciagi.append(akt)    

# print(podciagi)
# print('--------------')


# def najdluzszy(arr):
#     naj_dl = 0
#     najd_dl = []
#     ar=[]
#     for i in arr:
#         if len(i) > naj_dl:
#             naj_dl = len(i)
#     for i in arr:
#         if len(i) == naj_dl:
#             najd_dl.append(i)

#     for podciag in najd_dl:
#         ar.append(podciag)
        
#     print("Najdłuższe podciągi:", ar[0])
#     print('Najdłuższy:', naj_dl)
    
# najdluzszy(podciagi)






# zad 3

# arr = [2, 5, 8, 12, 15, 18, 21, 4, 7, 10, 13, 16, 19, 22, 1, 3, 16, 9, 16, 14, 17, 20, 23, 25, 24, 8, 5, 2, 1, 10, 1, 2, 3, 4, 5, 6, 7]
# podciagi=[]
# akt=[arr[0]]
# for i in range(1,len(arr)):
#     if arr[i] > arr[i-1]:
#         akt.append(arr[i])
#     else:
#         podciagi.append(akt)
#         akt = [arr[i]]
# podciagi.append(akt)    

# print(podciagi)
# print('--------------')


# def najdluzszy(arr):
#     naj_dl = 0
#     najd_dl = []
#     ar=[]
#     for i in arr:
#         if len(i) > naj_dl:
#             naj_dl = len(i)
#     for i in arr:
#         if len(i) == naj_dl:
#             najd_dl.append(i)

#     for podciag in najd_dl:
#         ar.append(podciag)
        
#     print("Najdłuższe podciągi:", ar)
#     print('Najdłuższy:', naj_dl)
    
# najdluzszy(podciagi)





# zad 4
# import random

# def generuj_tablice(najwie):
#     tablica = [random.randint(-najwie, najwie) for i in range(najwie)]
#     return tablica

# rozmiar_tablicy = 10
# arr = generuj_tablice(rozmiar_tablicy)
# print(arr)



# podciagi = []
# akt = [arr[0]]
# for i in range(1, len(arr)):
#     if arr[i] > arr[i - 1]:
#         akt.append(arr[i])
#     else:
#         podciagi.append(akt)
#         akt = [arr[i]]
# podciagi.append(akt)

# posortowane = sorted(podciagi, key=len)
# najdluzszy_podciag = posortowane[-1]
# print(najdluzszy_podciag)



# zad 5
# import random

# def generuj_tablice(najwie):
#     tablica = [random.randint(-najwie, najwie) for i in range(najwie)]
#     return tablica

# rozmiar_tablicy = 20
# arr = generuj_tablice(rozmiar_tablicy)


# podciagi=[]
# akt=[arr[0]]
# suma=0

# for i in range(1,len(arr)):
#     if arr[i] < 0:
#         if arr[i] > arr[i-1]:
#             akt.append(arr[i])
#         else:
#             for a in akt:
#                 suma+=a
#             podciagi.append(suma)
#             akt = [arr[i]]  
#             suma = 0 
        
        
# for a in akt:
#     suma+=a
# podciagi.append(suma)


        
# def ile(podciagi):
#     for c in set(podciagi):
#         print(f"{c} - {podciagi.count(c)} razy")
        
# print(f"tablica: {arr}")
# print(f"podciągi: {podciagi}")      
# ile(sorted(podciagi))














# zad 6 i 7

# import random

# def generuj_tablice(najwie):
#     tablica = [random.randint(0, najwie) for i in range(najwie)]
#     return tablica

# rozmiar_tablicy = 20
# arr = generuj_tablice(rozmiar_tablicy)


# podciagi=[]
# akt=[arr[0]]
# suma=0

# for i in range(1,len(arr)):
#     if arr[i] > arr[i-1]:
#         akt.append(arr[i])
#     else:
#         for a in akt:
#             suma+=a
#         podciagi.append(suma)
#         akt = [arr[i]]  
#         suma = 0 
# for a in akt:
#     suma+=a
# podciagi.append(suma)


        
# def ile(podciagi):
#     for c in set(podciagi):
#         print(f"{c} - {podciagi.count(c)} razy")
        
# print(f"tablica: {arr}")
# print(f"podciągi: {sorted(podciagi)}")      
# ile(sorted(podciagi))