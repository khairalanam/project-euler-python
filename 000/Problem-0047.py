import math


def prime_factors_count(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n >>= 1
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 2:
        factors.add(n)
    return len(factors)


def find_consecutive_numbers_with_distinct_prime_factors(target):
    consecutive_count, n = 0, 2
    while True:
        if prime_factors_count(n) == target:
            consecutive_count += 1
            if consecutive_count == target:
                return n - target + 1
        else:
            consecutive_count = 0
        n += 1


print(find_consecutive_numbers_with_distinct_prime_factors(4))
