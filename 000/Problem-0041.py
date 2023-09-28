"""
We shall say that an n-digit number is pandigital
if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
from itertools import permutations


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


a = '123456789'

flag = True

j = 9

while flag:
    p = permutations(a[: j])
    p = list(p)[:: -1]
    for i in p:
        if int(i[j - 1]) % 2:
            number = int(''.join(i))
            if (number + 1) % 6 == 0 or (number - 1) % 6 == 0:
                if is_prime(number):
                    print(number)
                    flag = False
                    break
    j -= 1
