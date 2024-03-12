tekst = input('Wczytaj tekst: ')
klucz = int(input('Wczytaj klucz (liczbę całkowitą): '))

def szyfr(t, klucz):
    global szyfrogram 
    szyfrogram = ''
    
    for i in t:
        if i.isalpha(): 
            kod = ord(i) + klucz
            if i.isupper():
                if kod > ord('Z'):
                    kod -= 26
            elif i.islower():
                if kod > ord('z'):
                    kod -= 26
            szyfrogram += chr(kod)
        else:
            szyfrogram += i

    print(szyfrogram)

szyfr(tekst, klucz)
