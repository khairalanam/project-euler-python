"""
The decimal number, 585 = 1001001001 (binary),
is palindromic in both bases.

Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.
"""


def is_palindrome(s):
    return s == s[::-1]


def find_double_base_palindromes(limit):
    double_base_palindromes = []

    for num in range(1, limit):
        decimal_str = str(num)
        binary_str = bin(num)[2:]
        if is_palindrome(decimal_str) and is_palindrome(binary_str):
            double_base_palindromes.append(num)

    return double_base_palindromes


print(sum(find_double_base_palindromes(1000000)))
