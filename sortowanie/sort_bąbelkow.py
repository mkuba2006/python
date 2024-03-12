import os

def sor():
    for i in range(length):
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                pom = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = pom





arr = [112,45,1,85,12,845,122];
length = 0
for i in  arr:
    length+=1







os.system('cls')
sor()
print(arr)