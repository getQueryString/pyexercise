# Copyright© by Fin

from math import sqrt
from random import randint

def randomZahl():
    randomnumb = randint(0, 100)    # min, max

    return randomnumb
    rand = randomZahl()
    wurzel(rand)
randomZahl()


def randomzahl():
    randomnumb1 = randint(0, 100)
    randomnumb2 = randint(0, 100)

    return randomnumb1, randomnumb2
    rand1 = randomzahl()
    calc(rand1)
randomzahl()


def calc(randomnumb1, randomnumb2):

    zahl1 = int(input(randomnumb1))
    zahl2 = int(input(randomnumb2))

    print("{} + {} =".format(zahl1, zahl2), zahl1 + zahl2)
    print("{} - {} =".format(zahl1, zahl2), zahl1 - zahl2)
    print("{} * {} =".format(zahl1, zahl2), zahl1 * zahl2)
    print("{} / {} =".format(zahl1, zahl2), zahl1 / zahl2)
calc()

def wurzel(randomnumb):

    wurzel = int(input(randomnumb))
    erg = sqrt(wurzel)
    print(f"Quadratwurzel {wurzel} ")
    print(erg)
wurzel()