import random
from bijectives_functions import * 

SEED = 1961
ALPHA = [ chr(ord('a') + i) for i in range(26) ]
A, B = 10, 555
a,b= 0.5, 8
ASKII = []

random.seed(SEED)
MAX_DECALAGE = random.uniform(a, b)

for a in ALPHA:
    while True:
        code = random.uniform(A, B)
        
        min_difference = float('inf') if not ASKII else min( c - code for c in ASKII )
        if min_difference < MAX_DECALAGE:
            continue

        ASKII[a] : code
    




# Liste des fonctions
BIJECTIVES_FUNCTIONS = [identity, exponential, logarithm, square_root, cube, inverse, sinus, tanh, arctan,
                       power_fractional, cosh, arcsin, tanh_squared, exp_power, tanh_sqrt, sinh, tan, cos_power,
                       log_tanh, arccos, sinh_squared, cube_sqrt, sin_sqrt, exp_tanh, arctan_sinh, power_tanh,
                       sin_power, tan_squared, exp_sinh, arctan_power, tanh_sqrt_squared, arcsin_tanh, sqrt_squared]



def decoder():
    pass
    



