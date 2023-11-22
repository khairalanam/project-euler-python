from math import isqrt


def is_square(n):
    root = isqrt(n)
    return root * root == n


def continued_fraction_period_length(n):
    m, d, a = 0, 1, isqrt(n)
    original_a = a
    period_length = 0

    while a != 2 * original_a:
        m = d * a - m
        d = (n - m * m) // d
        a = (original_a + m) // d
        period_length += 1

    return period_length


def count_odd_period_square_roots(limit):
    count = 0
    for N in range(2, limit + 1):
        if not is_square(N):
            period_length = continued_fraction_period_length(N)
            if period_length % 2 == 1:
                count += 1
    return count


print(count_odd_period_square_roots(10000))
