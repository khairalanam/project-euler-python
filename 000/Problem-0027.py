"""
Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| ≤ 1000

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def consecutive_prime_count(a, b):
    n = 0
    while True:
        value = n**2 + a * n + b
        if not is_prime(value):
            return n
        n += 1


def find_quadratic_coefficients(limit):
    max_primes = product = 0

    for a in range(-limit + 1, limit):
        for b in range(-limit, limit + 1):
            primes_count = consecutive_prime_count(a, b)
            if primes_count > max_primes:
                max_primes = primes_count
                product = a * b

    return product


print(find_quadratic_coefficients(1000))
