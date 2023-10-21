import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def randu (seed: int, iterations: int):
    i: int = 1

    while i <= iterations:
        seed = (seed * 65539) % 2**31
        i = i + 1

    return seed

def equation (seed: int, n: int):
    print(randu(seed, n))
    print(randu(seed, n+1))
    print(randu(seed, n+2))
    return randu(seed, n+2) == (randu(seed, n+1) * 6 - randu(seed, n) * 9) % 2**31

def carre (seed: int, iterations: int, n: int):
    i: int = 0
    x: list = []
    y: list = []
    j: int = 1
    section: float
    k: int = 1
    l: int = 1

    while i < iterations:
        seed = (seed * 65539) % 2**31
        x.append(float(seed)/2**31)
        seed = (seed * 65539) % 2**31
        y.append(float(seed)/2**31)

        i = i + 1

    plt.scatter(x,y,10)
    plt.show()

    heatmap_data = np.zeros((n, n))

    for i in range(iterations//2):
        x_index = int(x[i] * n)
        y_index = int(y[i] * n)

        x_index = min(x_index, n - 1)
        y_index = min(y_index, n - 1)

        heatmap_data[x_index, y_index] += 1

    sns.heatmap(heatmap_data, cmap='Blues', fmt='.0f')
    # plt.title('n = ' + str(n) + ' | Points générés = ' + str(iterations) + ' | Graine = ' + str(seed))
    plt.show()

carre(787945, 10000, 20)