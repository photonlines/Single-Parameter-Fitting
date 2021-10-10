from mpmath import sin, pi, almosteq, mp
from random import random

PRECISION = 8
mp.prec = PRECISION

def squared( num ):
    return num ** 2

def mod_one( num ):
    return num % 1

def phi( real_num ):
    return squared( sin( 2 * pi * real_num ) )

def dyadic_map( x ):
    return mod_one(2 * x)

CURRENT_ITER = random()
next_phi_iterate = phi( 2 * CURRENT_ITER )
next_dyadic_iterate = dyadic_map( CURRENT_ITER )

# Also, knowing that next_dyadic_map_iterate = dyadic_map( previous_iterate ), we can infer that:
assert almosteq( next_phi_iterate, phi( next_dyadic_iterate) )

print( 'NEXT PHI ITERATE: ', str( next_phi_iterate ))
print( 'PHI OF NEXT DYADIC ITERATE: ', str( phi( next_dyadic_iterate) ))