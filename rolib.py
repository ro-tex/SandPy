'''This is a PoC module.
'''

import math


def hello():
    return 'Hello from RoLib!'


def lcm(x, y):
    'Returns the Least Common Multiple of x and y'
    factors_x = factor(x)
    factors_y = factor(y)

    for f in factors_y:
        if factors_y.count(f) > factors_x.count(f):
            for _ in range(factors_y.count(f) - factors_x.count(f)):
                factors_x.append(f)

    lcm = 1
    for i in factors_x:
        lcm = lcm * i

    return lcm


def factor(n):
    'Returns an array with all prime number factors that make up n'
    if n < 2:
        return []

    for x in range(2, int(math.sqrt(n)) + 1):
        if is_prime(x) and n % x == 0:
            return [x] + factor(int(n / x))
    return [n]


def is_prime(n):
    if n <= 1 or (n > 2 and n % 2 == 0):
        return False

    # try dividing by all odd numbers between 3 and the square root of n:
    for x in xrange(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False

    return True
