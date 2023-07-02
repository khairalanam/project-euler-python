"""
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

Problem: What is the 10001st prime number?
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

def prime_find(n: int) -> int:
    """
    function: Find the nth prime number
    params: n: int
    returns: int
    """
    count = result = 1

    while count != n:
        result += 2
        if is_prime(result):
            count += 1

    return result

print(prime_find(10001))
