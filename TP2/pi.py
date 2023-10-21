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
    


def pi(N: int, rand: str, seed: int):
    i: int = 1
    s: int = 0
    x: float
    y: float
    lenght = len(str(seed))

    while i <= N*2:

        if rand == "python":
            x = random.random()
            y = random.random()

        elif rand == 'randu':
            seed = (seed * 65539) % 2**31
            x = float(seed)/2**31
            seed = (seed * 65539) % 2**31
            y = float(seed)/2**31

        elif rand == 'neumann':
            seed = rand_von(seed, lenght)
            x = float(seed) / (10**lenght-1)
            seed = rand_von(seed, lenght)
            y = float(seed) / (10**lenght-1)
            
        else:
            return

        if math.sqrt(x**2 + y**2) <=1:
            s = s + 1
        i = i + 2
    
    return(s * 4 / N)


def aprox_pi(n: int):
    x: list = []
    y: list = []
    i: int = 10

    while i <= n:
        y.append(pi(i, 'randu', 89454218954198595615151269561))
        x.append(i)
        i = i + 10


    plt.scatter(x, y, 1)
    plt.axhline(y=math.pi, color="r",linewidth=1)
    plt.show()

aprox_pi(10000)