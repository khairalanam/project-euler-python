"""
An irrational decimal fraction is created
by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the following expression:

d_1 x d_10 x d_100 x d_1000 x d_10000 x d_100000 x d_1000000
"""

def champernowne_constant_digit(n):
    constant = ""
    i = 1

    while len(constant) < n:
        constant += str(i)
        i += 1

    return int(constant[n - 1])

indices = [1, 10, 100, 1000, 10000, 100000, 1000000]
result = 1

for index in indices:
    result *= champernowne_constant_digit(index)

print(result)
