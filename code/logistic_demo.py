from functools import reduce
from mpmath import mp, power, sin, pi, asin, sqrt
import numpy as np

PRECISION = 10

# Seed value:
SEED = 42
np.random.seed(SEED)

def print_separator(num_dashes=120):
    print('-' * num_dashes)

# First, let's create a dataset composed of random data points:
NUM_DATA_POINTS = 100
DATA = np.random.uniform(0, 1, NUM_DATA_POINTS)

# Mpmath uses a global working precision. We calculate the global precision value we need and set it accordingly.
MP_PRECISION = NUM_DATA_POINTS * PRECISION
mp.prec = MP_PRECISION

print("DATA: ", str(DATA))
print_separator()

# Functions which we're going to use to encode and decode our data:

def squared( num ):
    return num ** 2

def phi( real_num ):
    return squared( sin( 2 * pi * real_num ) )

def inverse_phi( real_num ):
    return asin( sqrt( real_num )) / (2 * np.pi)

def mod_one( num ):
    return num % 1

def dyadic_map( x ):
    return mod_one(2 * x)

def two_to_the_power_of(num):
    return power(2, num)

def decimal_to_binary( real_num, precision = PRECISION):

    def convert_to_binary_string(num):
        return '0' if num < 0.5 else '1'

    return reduce(
        # The function to use to reduce our data set. The accumulator represents our aggregated result, while
        # x represents the next element to process within our sequence:
        lambda accumulator, next_element: [
            dyadic_map( accumulator[0] ), accumulator[1] + convert_to_binary_string(accumulator[0])
        ]
        # The sequence of values to perform our reduce operation on
        , range( precision )
        # If an initial value is present, it is placed before the items of the sequence in the calculation, and serves
        # as a default when the sequence is empty. Here, we start off with a 2 element array, with the first
        # element representing our decimal number, and the 2nd element which holds our binary representation:
        , [real_num, '']
    ) [1] # Note that we return the 2nd element in our reduction, which holds our binary representation!

def binary_to_decimal( binary_num ):

    return reduce (
        # Function
        lambda accumulator, next_element:
            accumulator + int(next_element[1]) / two_to_the_power_of(next_element[0] + 1)
        # Sequence: Iterate over the binary digits / representation
        , enumerate( binary_num )
        # Initial: We initialize it to a real/floating point value of 0.0
        , mp.mpf(0.0)
    )

def binary_conjugate( data ):
    decimal_to_binary_phi_inverse = lambda z : decimal_to_binary( inverse_phi( z ), PRECISION )
    return ''.join( map( decimal_to_binary_phi_inverse, data) )

# Finally, we can demo the encoding and decoding process and show the results:

binary_conjugate_str = binary_conjugate( DATA )

print( 'BINARY CONJUGATE: ' , binary_conjugate_str )
print_separator()

decimal_conjugate = binary_to_decimal( binary_conjugate_str )

print( 'DECIMAL CONJUGATE: ' , decimal_conjugate )
print_separator()

decimal = phi( decimal_conjugate )

print( 'DECIMAL: ' , str(decimal) )
print_separator()

def logistic_decoder (
    real_num
    , time_step
    , precision = PRECISION
):
    return float(
        squared(
            sin(
                two_to_the_power_of( time_step * precision ) * asin( sqrt( real_num ) )
            )
        )
    )

decoded_values = [
    float( logistic_decoder( real_num = decimal, time_step = time_idx) )
    for time_idx
    in range(NUM_DATA_POINTS)
]

print( "DECODED VALUES: ", str( np.array( decoded_values ) ) )