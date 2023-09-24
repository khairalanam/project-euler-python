"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576

By concatenating each product, we get the 1-to-9
pandigital, 192384576. We will call this a
"pan-digital product."

What is the largest 1-to-9 pandigital 9-digit number
that can be formed as the concatenated product of an
integer with (1,2, ... , n) where n > 1?
"""


def is_pandigital(s):
    return ''.join(sorted(s)) == '123456789'


largest_pandigital = 0

for num in range(1, 10000):
    concatenated_product = ''
    n = 1

    while len(concatenated_product) < 9:
        concatenated_product += str(num * n)
        n += 1

    if len(concatenated_product) == 9 and is_pandigital(concatenated_product):
        largest_pandigital = max(largest_pandigital, int(concatenated_product))

print(largest_pandigital)
