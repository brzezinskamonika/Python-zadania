def funkcja():
    a = int(input('pierwsza liczba sumy:'))
    b = int(input('ostatnia liczba sumy:'))
    suma=[]
    for n in range(a,b+1):
        suma.append(n)
    print(sum(suma))

funkcja()
        