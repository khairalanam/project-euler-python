"""
The sum of the primes below 10 is
2 + 3 + 5 + 7 = 17

Problem: Find the sum of all the primes below two million
"""


from math import sqrt


def is_prime(n: int) -> bool:
    """
    function: Check whether n is prime
    params: n: int
    returns: bool
    """

    # prime checking for number 1 - 10 and numbers and divisible by 2 and 3
    if n == 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False

    # Every prime number > 3 can be written as 6k - 1 or 6k + 1
    n_sqrt = int(sqrt(n))
    f = 5

    while f <= n_sqrt:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6

    return True
