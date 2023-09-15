"""
145 is a curious number, as
1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which
are equal to the sum of the factorial
of their digits.

Note: As 1! = 1 and 2! = 2 are not sums,
they are not included.
"""

from math import factorial


def is_digit_factorial_sum(number):
    digit_factorial_sum = sum(factorial(int(digit)) for digit in str(number))
    return digit_factorial_sum == number


def find_digit_factorial_sums():
    digit_factorial_sums = 0
    for number in range(10, 2540160):
        if is_digit_factorial_sum(number):
            digit_factorial_sums += number

    return digit_factorial_sums


print(find_digit_factorial_sums())
