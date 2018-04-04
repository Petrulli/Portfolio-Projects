## this program will calculate PI & e to the Nth. digit

import numpy as np

def pi_decimal(x):
    return ("%." + str(x) + "f") %np.pi

result = pi_decimal(2)
print(result)

def e_decimal(y):
    return ("%." + str(y) + "f") %np.e

print(e_decimal(2))