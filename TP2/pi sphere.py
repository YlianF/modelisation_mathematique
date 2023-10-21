import random
import math
import matplotlib.pyplot as plt

def rand_von (seed: int, seedLenght) :
    lenght: int

    seed = seed * seed

    lenght = len(str(seed))

    start = lenght//2 - seedLenght//2

    seed = int(str(seed)[ start : start + seedLenght ])

    return seed



def pi(N: int):
    i: int = 1
    s: int = 0
    x: float
    y: float
    z: float
    # xlist: list = []
    # ylist: list = []
    # zlist: list = []

    while i <= N:

        x = random.random()
        y = random.random()
        z = random.random()

        if math.sqrt(x**2 + y**2 + z**2) <=1:
            # xlist.append(x)
            # ylist.append(y)
            # zlist.append(z)
            s = s + 1

        i = i + 1

    # fig = plt.figure()
    # ax = fig.add_subplot(projection='3d')
    # ax.scatter(xlist, ylist, zlist)
    # plt.show()

    return(s * 8 / N)


def aprox_pi(n: int):
    x: list = []
    y: list = []
    i: int = 1

    while i <= n:
        y.append(pi(i))
        x.append(i)
        i = i + 100

    plt.scatter(x, y, 1)
    plt.axhline(y=(4/3)*math.pi, color="r",linewidth=1)
    plt.show()

aprox_pi(100000)

