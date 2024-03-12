

# def lider(len,arr):
#     min = len//2 + 1
#     print("arr: ", sorted(arr))
#     print("len:", len)
#     print("min:",min)
    
#     ile_lider = None
#     jaka = None
    
#     for i in arr:
#         akt = arr.count(i)
#         if akt >= min:
#             jaka = i
#             ile_lider = akt

#     print("Lider", jaka,":",ile_lider,"razy")
      
      
      
        
# arr =[1,2,3,1,1,1,1,9]
# len = len(arr)
    
# lider(len,arr)



tablica = [1,1,1,2,2] 
minimum = len(tablica) // 2 + 1

jaka_liczba = None
ile = None

for i in tablica:
    ile_aktualna = tablica.count(i)
    if ile_aktualna >= minimum:
        jaka_liczba = i
        ile = ile_aktualna

print(jaka_liczba)
print(ile) 































