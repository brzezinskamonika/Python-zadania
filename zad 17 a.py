from matplotlib import pyplot as plt

#a) fukcję liniową ax+b
def liniowa(a, b):
    xaxis = []
    yaxis = []
    for x in range(0, 100):
        xaxis.append(x)
        yaxis.append(a*x + b)
        
    return xaxis, yaxis

x, y = liniowa(1, 2)
plt.plot(x, y)