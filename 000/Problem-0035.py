"""
The number, 197, is called a circular
prime because all rotations of the
digits: 197, 971, and 719, are
themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below n?
"""


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_circular_prime(n):
    num_str = str(n)
    num_len = len(num_str)
    for _ in range(num_len):
        if not is_prime(int(num_str)):
            return False
        num_str = num_str[1:] + num_str[0]
    return True


def count_circular_primes(limit):
    count = 0
    for num in range(2, limit):
        if is_circular_prime(num):
            count += 1
    return count


print(count_circular_primes(1000000))
