import numpy as np

def skosnosc(x):
    n=len(x)
    srednia=np.mean(x)
    skos=[]
    for i in range(n):
        skos.append(float((x[i]-srednia)**3))
    print('skosnosc wynosi ' + str(sum(skos)/n))
        
    
lista=[5.5,5.8,14.12,28.3,25.5,3.9,1.1]

skosnosc(lista)

