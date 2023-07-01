"""
The sum of the squares of the first ten natural numbers is:
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is:
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares
of the first ten natural numbers and the square of
the sum is:
3025 - 385 = 2640

Problem: Find the difference between the sum of the squares
of the first one hundred natural numbers and the square of the sum.
"""

"""
Formula for the sum of the first n natural numbers:
1 + 2 + 3 + 4 + 5 + 6 + . . . + n = n(n + 1) / 2

Formula for the sum of squares of first n natural numbers:
1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2 + . . . + n^2 = n(n + 1)(2n + 1) / 6
"""
def sum_square_difference(n):
    return ((n * (n + 1) // 2) * (n * (n + 1) // 2)) - (n * (n + 1) * ((2 * n) + 1) // 6)

print(sum_square_difference(100))