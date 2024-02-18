arr = [1,2,3,4,5,6,6,6,6,6,6]; #lider 6 , 6 razy


def szukaj_lider(arr):
    kandydat = arr[0]
    ile = 1
    minimalna = len(arr) // 2 + 1
    
    for i in range (0,len(arr)):
        if ile == 0:
            kandydat= arr[i]
            ile = 1
        elif kandydat == arr[i]:
            ile += 1
        else:
            ile -= 1
    
    print("min", minimalna)
    if ile >= minimalna:
        print("lider:",kandydat)
        print(ile,"razy")
    else:
        print("brak kandydata")
    
    
szukaj_lider(arr)