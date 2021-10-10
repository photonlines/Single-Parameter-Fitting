from functools import reduce
from mpmath import mp, power
import numpy as np

PRECISION = 10

# Seed value:
SEED = 42
np.random.seed(SEED)

def print_separator(num_dashes=120):
    print('-' * num_dashes)

# First, lets create a dataset composed of random data points:
NUM_DATA_POINTS = 100
DATA = np.random.uniform(0, 1, NUM_DATA_POINTS)

# Mpmath uses a global working precision, so we calculate the required precision we need to work with
# and set it to an appropriate value:
MP_PRECISION = NUM_DATA_POINTS * PRECISION
mp.prec = MP_PRECISION

print("DATA: ", str(DATA))
print_separator()

# Functions which we're going to use to encode and decode our data:

def mod_one(num):
    return num % 1

def dyadic_map(x):
    return mod_one(2 * x)

def two_to_the_power_of(num):
    return power(2, num)

def decimal_to_binary(real_num, precision=PRECISION):
    def convert_to_binary_string(num):
        return '0' if num < 0.5 else '1'

    # The reduce function iterates over all elements of a list/array and returns one value which is composed
    # of an accumulated result of an operation performed through a passed in lambda function:
    return reduce(
        # The function to use to reduce our data set. The accumulator represents our aggregated result, while
        # x represents the next element to process within our sequence:
        lambda accumulator, next_element: [
            dyadic_map(accumulator[0]), accumulator[1] + convert_to_binary_string(accumulator[0])
        ]
        # The sequence of values to perform our reduce operation on
        , range(precision)
        # If an initial value is present, it is placed before the items of the sequence in the calculation, and serves
        # as a default when the sequence is empty. Here, we start off with a 2 element array, with the first
        # element representing our decimal number, and the 2nd element which holds our binary representation:
        , [real_num, '']
    )[1]  # Note that we return the 2nd element in our reduction, which holds our binary representation!

def binary_to_decimal(binary_num):
    return reduce(
        # Reduce function:
        lambda accumulator, next_element:
        accumulator + int(next_element[1]) / two_to_the_power_of(next_element[0] + 1)

        # Sequence: Iterate over the binary digits / representation
        , enumerate(binary_num)

        # Initial: We initialize it to a real/floating point value of 0.0
        , mp.mpf(0.0)
    )

# Finally, we can demo the encoding and decoding process and show the results:

binary_representation = ''.join(map(decimal_to_binary, DATA))

print('BINARY REPRESENTATION: ', str(binary_representation))
print_separator()

decimal = binary_to_decimal(binary_representation)

print('DECIMAL REPRESENTATION: ', str(decimal))
print_separator()

def dyadic_decoder(real_num, time_step, precision=PRECISION):
    return mod_one(
        two_to_the_power_of(time_step * precision) * real_num
    )

decoded_values = [
    float(dyadic_decoder(real_num=decimal, time_step=time_idx))
    for time_idx
    in range(NUM_DATA_POINTS)
]

print("DECODED VALUES: ", str(np.array(decoded_values)))