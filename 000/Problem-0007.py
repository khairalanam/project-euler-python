"""
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

Problem: What is the 10001st prime number?
"""

from math import sqrt

def is_prime(n: int):
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

    n_sqrt = int(sqrt(n))
    f = 5

    while f <= n_sqrt:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6

    return True

def prime_check(n: int):
    count = result = 1

    while count != n:
        result += 2
        if is_prime(result):
            count += 1

    return result

print(prime_check(10001))
