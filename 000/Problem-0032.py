"""
We shall say that an n-digit number is pandigital
if it makes use of all the digits 1 to n exactly
once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity,
39 x 186 = 7254, containing multiplicand,
multiplier, and product is 1 through 9
pandigital.

Find the sum of all products whose multiplicand/
multiplier/product identity can be written as a
1 through 9 pandigital.

Note: Some products can be obtained in more than
one way, so make sure to only include the
distinct sums in your answer.
"""


def is_pandigital_product(multiplicand, multiplier, product):
    all_digits = str(multiplicand) + str(multiplier) + str(product)
    return ''.join(sorted(all_digits)) == '123456789'


pandigital_products = set()

for multiplicand in range(1, 100):
    for multiplier in range(1, 10000):
        product = multiplicand * multiplier
        if len(str(multiplicand) + str(multiplier) + str(product)) > 9:
            break
        if is_pandigital_product(multiplicand, multiplier, product):
            pandigital_products.add(product)

print(sum(list(pandigital_products)))
