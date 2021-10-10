# mpmath is a free BSD-licensed library for real and complex floating-point arithmetic with arbitrary precision.
from mpmath import sin, asin, sqrt

def two_to_the_power_of(num):
    return 2 ** num

def squared(num):
    return num ** 2

def logistic_decoder(
        # The real-valued number to be learned / generated from the data
        real_num
        # A series of integer values
        , x
        # The precision is a constant which controls our accuracy
        , precision = 12
):
    return float(
        squared(
            sin(
                two_to_the_power_of(x * precision) * asin(sqrt(real_num))
            )
        )
    )
