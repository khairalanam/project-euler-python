"""
A palindromic number reads the same both ways.
The largest palindromic number made from the product of
two 2-digit numbers is 9009 = 99 x 91

Problem: Find the largest palindromic number made
from the product of two 2-digit numbers.
"""

def is_palindrome(n: int):
    n = str(n)
    return n == n[::-1]

def largest_palindromic_product():
    max_prod = 0

    # loop from 999 to 100
    for i in range(999, 99, -1):

        # loop from i to 100 rather than 999 to 100. Prevents from unnecessary
        # checking of the older products
        
        for j in range(i, 99, -1):
            if is_palindrome(( res := i * j )):
                max_prod = max(max_prod, res)

    return max_prod

print(largest_palindromic_product())