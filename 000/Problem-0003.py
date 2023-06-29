"""
The prime factors of 13195 are 5, 7, 13, and 25.

Problem: What is the largest prime factor
of the number 600851475143?
"""

from math import sqrt, floor

def is_prime(num: int):

    """
    function: Check whether the integer num is prime or not
    params: num of int type
    """

    num_sqrt = floor(sqrt(num))

    for i in range(2, num_sqrt):
        if num % i == 0:
            return False

    return True

def largest_prime_factor(n: int):

    """
    function: returns the largest prime factor of the number n
    params: n of int type
    """

    num = floor(sqrt(n))
    factors = []

    # This loop returns all the factors of n in descending order
    for i in range(num, 1, -1):
        if n % i == 0:
            factors += [i]

    # This loop goes through the factors and returns the largest prime factor
    for i in factors:
        if i % 2 and is_prime(i):
            return i

    return -1

print(largest_prime_factor(600851475143))