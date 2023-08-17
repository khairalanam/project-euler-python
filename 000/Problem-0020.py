"""
n! means n factorial, which is the product of
all positive integers less than or equal to n.

For example, 10! = 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1
= 3,628,800, and the sum of the digits in the number is
3 + 6 + 2 + 8 + 8 + 0 + 0 + 0 = 27.

Problem: Find the sum of the digits in the number 100!.
"""
from math import factorial


def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))


print(sum_of_digits(factorial(100)))
