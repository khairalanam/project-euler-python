from math import factorial


def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


def count_combinations_over_million(limit):
    count = 0
    for n in range(1, limit + 1):
        for r in range(1, n + 1):
            if combinations(n, r) > 1000000:
                count += 1
    return count


print(count_combinations_over_million(100))
