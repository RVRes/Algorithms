import math as m

INTEGRALF = lambda x: m.sin(x)
ACCURACY = 10000000
LIMIT_LOW = 0
LIMIT_HI = 10


def integral_count(fnct: callable, acc: int, l_hi: int, l_lo: int) -> float:
    result = 0
    step = (l_hi - l_lo) / acc
    cur_point = l_lo
    l_hi -= step
    while cur_point < l_hi:
        result += fnct(cur_point)*step
        cur_point += step
    return round(result, 6)


print(integral_count(INTEGRALF, ACCURACY, LIMIT_HI, LIMIT_LOW))
