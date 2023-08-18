"""
Let d(n) be defined as the sum of proper divisors
of n (numbers less than n which divide evenly into n).

If d(d(n)) = n and d(n) ≠ n, then n is an "amicable number."

For example, the proper divisors of 220 are 1, 2, 4,
5, 10, 11, 20, 22, 44, 55, and 110, and their sum is
284. The proper divisors of 284 are 1, 2, 4, 71, and 142,
and their sum is 220.

Evaluate the sum of all amicable numbers under 10000.
"""
from math import sqrt


def sum_of_proper_divisors(n):
    divisors = [1]
    x = int(sqrt(n)) + 1
    for i in range(2, x):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)


def find_amicable_numbers(limit):
    amicable_numbers = []
    for num in range(2, limit):
        if num not in amicable_numbers:
            div_sum = sum_of_proper_divisors(num)
            if div_sum != num and sum_of_proper_divisors(div_sum) == num:
                amicable_numbers.extend([num, div_sum])
    return amicable_numbers


print(sum(find_amicable_numbers(10000)))
