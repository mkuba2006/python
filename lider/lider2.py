def lider(arr):
    kandydat = arr[0]
    ile = 1
    min = len(arr) // 2 + 1
    print('min:',min)
    
    for i in range(1,len(arr)):
        if ile == 0:
            kandydat = arr[i]
            ile = 1
        elif arr[i] == kandydat:
            ile += 1
        else:
            ile -= 1
        
    ile_kandydata = arr.count(kandydat)
    
    
    if ile_kandydata >= min:
        print("lider: ", kandydat)
        print(ile_kandydata,'razy')
    else:
        print('nie ma lidera')
        
arr = [1,1,1,4,3]
lider(arr)




