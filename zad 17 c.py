from matplotlib import pyplot as plt

#c) funkcję odwrotnie-potęgową a/x^n
def odwrotniepotegowa(a, n):
    xaxis = []
    yaxis = []
    for x in range(1, 100):
        xaxis.append(x)
        yaxis.append(a/(x**n))
        
    return xaxis, yaxis

x, y = odwrotniepotegowa(1, 2)
plt.plot(x, y)