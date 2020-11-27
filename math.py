# Copyright© by Fin

from math import sqrt
from random import randint

def Wurzel():
    rnumb = randint(0, 1000)
    erg = sqrt(rnumb)
    rerg = round(erg, 4)
    print(f"\nWurzel()\nQuadratwurzel von {rnumb} ist {rerg}")

def Calc():
    rnumb1 = randint(0, 1000)
    rnumb2 = randint(0, 1000)
    divi = rnumb1 / rnumb2
    divide = round(divi, 4)

    print("\nClac()\n{} + {} =".format(rnumb1, rnumb2), rnumb1 + rnumb2)
    print("{} - {} =".format(rnumb1, rnumb2), rnumb1 - rnumb2)
    print("{} * {} =".format(rnumb1, rnumb2), rnumb1 * rnumb2)
    print("{} / {} =".format(rnumb1, rnumb2), divide)

Wurzel()
Calc()