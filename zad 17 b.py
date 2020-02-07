from matplotlib import pyplot as plt

#b) funkcję kwadratową ax^2+bx+c
def kwadratowa(a, b, c):
    xaxis = []
    yaxis = []
    for x in range(0, 100):
        xaxis.append(x)
        yaxis.append(a*(x**2) + b*x + c)
        
    return xaxis, yaxis

x, y = kwadratowa(1, 2, 3)
plt.plot(x, y)