import matplotlib.pyplot as plt


def rand_von (seed: int, iterations: int) :
    i: int = 1
    lenght: int
    seedLenght: int
    seedlist: list = []
    itlist: list = []

    seedLenght = len(str(seed))

    while i <= iterations: 
        itlist.append(i)
        seed = seed * seed
        i = i + 1
        lenght = len(str(seed))

        start = lenght//2 - seedLenght//2
        
        seed = int(str(seed)[ start : start + seedLenght ])
        seedlist.append(seed)


    plt.scatter(itlist,seedlist,1)
    plt.show() 

rand_von(4148623215, 100000)