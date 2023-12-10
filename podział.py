n= int(input("wczytaj :"))

def podział(n):
    if n <10:
        print(n)
    else:
        podział(int(n / 10))
        print(n%10)
podział(n)