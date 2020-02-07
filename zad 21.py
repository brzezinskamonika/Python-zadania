import numpy as np

def srednia(x):
    suma=sum(x)
    ilosc=len(x)
    return suma/ilosc
    
lista=[5.5,5.8,14.12,28.3,25.5,3.9,1.1]
print(np.mean(lista))
print(srednia(lista))