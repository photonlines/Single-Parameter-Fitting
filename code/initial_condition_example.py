from mpmath import sin, pi
from random import random

def squared( num ):
    return num ** 2

def phi( real_num ):
    return squared( sin( 2 * pi * real_num ) )

# The real number below should be constructed via the methodology we outlined previously -- we
# simply use a random value here to demo the equations shown in the paper
real_num = random()
INITIAL_CONDITION = phi(real_num)