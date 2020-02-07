import math
import numpy as np

def odchylenie(x):
    n=len(x)
    srednia=np.mean(x)
    standard=[]
    for i in range(n):
        standard.append(float((x[i]-srednia)**2))
    print('odchylenie standardowe wynosi ' + str(math.sqrt(sum(standard)/n)))
        
    
lista=[5.5,5.8,14.12,28.3,25.5,3.9,1.1]

odchylenie(lista)
#sprawdzenie:
print(np.std(lista))