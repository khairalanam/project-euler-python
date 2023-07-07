"""
The sequence of triangle numbers is generated
by adding the natural numbers. So, the 7th triangle number would be
1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.

The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:
1: 1
3: 1, 3
6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28

We can see that 28 is the first triangle number to have over five divisors.

Problem: What is the value of the first triangle number to have over five hundred divisors?
"""

import time


def get_triangle_number(n):
    return (n * (n + 1)) // 2


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(end - start)

        return res

    return wrapper


def is_prime(n: int) -> bool:
    """
    function: Check whether n is prime
    params: n: int
    returns: bool
    """

    # prime checking for number 1 - 10 and numbers and divisible by 2 and 3
    if n == 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False

    # Every prime number > 3 can be written as 6k - 1 or 6k + 1
    n_sqrt = int(n ** 0.5)
    f = 5

    while f <= n_sqrt:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6

    return True


def no_of_divisors_with_prime(n: int):
    if n == 1:
        return 1

    if is_prime(n):
        return 2

    n_sqrt = int(n ** 0.5)
    count = 2

    if n == n_sqrt * n_sqrt:
        count += 1

    for i in range(2, n_sqrt):
        if n % i == 0:
            count += 2

    return count


def no_of_divisors(n: int):
    if n == 1:
        return 1

    n_sqrt = int(n ** 0.5)
    count = 2

    if n == n_sqrt * n_sqrt:
        count += 1

    for i in range(2, n_sqrt):
        if n % i == 0:
            count += 2

    return count


@timer
def find_triangle_number(count: int):
    n = curr = 1

    while curr <= count:
        res = get_triangle_number(n)
        curr = no_of_divisors(res)
        n += 1

    return res


@timer
def find_triangle_number_with_prime(count: int):
    n = curr = 1

    while curr <= count:
        res = get_triangle_number(n)
        curr = no_of_divisors_with_prime(res)
        n += 1

    return res


print(find_triangle_number(500))
print(find_triangle_number_with_prime(500))
