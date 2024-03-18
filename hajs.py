import math

nominały=[500,200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
reszta = 108.21

for i in nominały:
    ile_wejdzie = math.floor(reszta / i)
    reszta = round(reszta - ile_wejdzie * i,2)
    if ile_wejdzie>0:
        print(i,"x", ile_wejdzie)
