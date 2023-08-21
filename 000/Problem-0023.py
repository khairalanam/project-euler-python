"""
A perfect number is a number for which the sum
of its proper divisors is exactly equal to the
number. For example, the sum of the proper
divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its
proper divisors is less than n, and it is called
abundant if this sum exceeds n.

As 12 is the smallest abundant number,
1 + 2 + 3 + 4 + 6 = 16, the smallest number that
can be written as the sum of two abundant numbers
is 24. By mathematical analysis, it can be shown
that all integers greater than 28123 can be written
as the sum of two abundant numbers. However, this upper
limit cannot be reduced any further by analysis, even
though it is known that the greatest number that cannot
be expressed as the sum of two abundant numbers is less
than this limit.

Find the sum of all positive integers that cannot be
written as the sum of two abundant numbers.
"""


def sum_of_proper_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)


def is_abundant(n):
    return sum_of_proper_divisors(n) > n


def find_abundant_numbers(limit):
    return [num for num in range(12, limit) if is_abundant(num)]


def find_non_abundant_sum_numbers(limit):
    abundant_numbers = find_abundant_numbers(limit)
    abundant_sums = [False] * (limit + 1)

    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            abundant_sum = abundant_numbers[i] + abundant_numbers[j]
            if abundant_sum <= limit:
                abundant_sums[abundant_sum] = True
            else:
                break

    non_abundant_sum_numbers = [
        i for i, is_sum in enumerate(abundant_sums) if not is_sum]
    return non_abundant_sum_numbers


print(sum(find_non_abundant_sum_numbers(28123)))
