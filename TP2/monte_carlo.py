import random
import math
import matplotlib.pyplot as plt

def monteCarlo(N: int, a: int, b: int):
    i: int = 1
    s: int = 0

    while i <= N:
        rand = random.random()*(b-a)+a
        s = s + rand**2
        i = i + 1

    res = (b - a) / N * s

    return res


def pi(N: int):
    i: int = 0
    s: int = 0
    x: float
    xlist: list = []
    y: float
    ylist: list = []

    while i< N:
        x = random.random()
        y = random.random()
        if math.sqrt(x**2 + y**2) <=1:
            s = s + 1
            xlist.append(x)
            ylist.append(y)
        i = i + 1
    
    print(s * 4 / N)

    plt.scatter(xlist, ylist, 5)
    plt.show()

print(pi(10000))