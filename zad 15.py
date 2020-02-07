from pylab import plot,show,legend,title,xlabel,ylabel

LagunaHills=[20,20,18,18,19,18,17,18,19,20,22,22,23,19]
Poznan=[5,5,9,10,5,4,5,4,5,8,8,9,10,8]
Strasburg=[6,11,14,11,9,8,8,10,10,12,13,13,13,9]

dni=range(1,15)

plot(dni,LagunaHills,marker="o")
plot(dni,Poznan,marker="v")
plot(dni,Strasburg,marker="x")
ylabel("Temperatura")
xlabel("Dni")
title("Różnica temperatur w trzech miastach w ciągu czternastu dni")
legend(['Laguna Hills','Poznań','Strasburg'])
show()