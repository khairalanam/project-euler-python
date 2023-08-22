"""
A permutation is an ordered arrangement of
objects. For example, 3124 is one possible
permutation of the digits 1, 2, 3, and 4.
If all of the permutations are listed
numerically or alphabetically, we call it
lexicographic order. The lexicographic
permutations of 0, 1, and 2 are:

012 021 102 120 201 210

What is the millionth lexicographic permutation of the digits 0 through 9?
"""

from math import factorial


def find_lexicographic_permutation(digits, n):
    permutation = []
    available_digits = list(digits)
    total_permutations = factorial(len(digits))

    n -= 1
    for i in range(len(digits)):
        total_permutations //= len(available_digits)
        index, n = divmod(n, total_permutations)
        digit = available_digits.pop(index)
        permutation.append(digit)

    return ''.join(permutation)


print(find_lexicographic_permutation("0123456789", 1000000))
