with open('bin.txt') as t:
    lines = t.readlines()

# def zamien(line):
#     binary_number = line.strip()
#     decimal_number = int(binary_number, 2)
#     print(decimal_number)


def zamiennadzies(line):
    cutted = line.strip()
    length = 0
    wartosc = 0
    najwieksza = 0
    poprzednia = int(cutted[0])
    
    for i in cutted:
        length += 1
    
    for i in range(length):
        liczba = int(cutted[length - 1 - i])
        power = 1
        for _ in range(i):
            power *= 2

        wartosc += liczba * power
        
    #     if liczba > poprzednia:
    #         najwieksza = liczba
        
    #     poprzednia = liczba

    # print("Wartosc:", wartosc)
    # print("Najwieksza:", najwieksza)
    print(wartosc)
    




for line in lines:
    zamiennadzies(line)

# for line in lines:
#     zamien(line.strip())

