def two_to_the_power_of( num ):
    return 2 ** num

def mod_one( num ):
    return num % 1

def dyadic_decoder( real_num, time_step, precision ):
    return mod_one(
        two_to_the_power_of( time_step * precision ) * real_num
    )