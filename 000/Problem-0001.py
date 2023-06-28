"""
If we list all the natural numbers below 10
that are multiples of 3 or 4, we get 3, 5, 6, and 9.
The sum of these multiples is 23.

Problem: Find the sum of all the multiples of
3 or 5 below 1000.
"""

def sum_of_three_or_five(n):
    res = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            res += i

    return res

print(sum_of_three_or_five(1000))