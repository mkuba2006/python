
def lider(len,arr):
    min = len//2 + 1
    print("arr: ", sorted(arr))
    print("len:", len)
    print("min:",min)
    
    ile_lider = None
    jaka = None
    
    for i in arr:
        akt = arr.count(i)
        if akt >= min:
            jaka = i
            ile_lider = akt

    print("Lider", jaka,":",ile_lider,"razy")
      
      
      
        
arr =[1,2,3,1,1,1,1,9]
len = len(arr)
    
lider(len,arr)