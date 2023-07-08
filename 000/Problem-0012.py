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

"""
Logic: This program goes for the brute force method by following these steps:
1. Generate the triangle number for each iteration
2. Count the number of divisors
3. Run the loop until the number of divisors exceed the
   required number of divisors, i.e., 500 in this case

The optimisation is done for finding the number of divisors.
Instead of iterating through all the numbers until the number,
we only run the loop until the square root of the number.
This way, we don;t have to increment the count by 1 and instead,
increment by 2.

That is, if n % i == 0, then that means i and n / i are divisors.
"""


def get_triangle_number(n: int) -> int:
    """
    function: To get the nth triangle number
    params: number n of type int
    returns: triangle number of type int
    """
    return (n * (n + 1)) // 2


def no_of_divisors(n: int) -> int:
    """
    function: find the number of divisors
    params: number n of type int
    function: returns the number of divisors of type int
    """
    if n == 1:
        return 1

    n_sqrt = int(n ** 0.5)
    count = 2

    # if n is a perfect square
    if n == n_sqrt * n_sqrt:
        count += 1

    for i in range(2, n_sqrt):
        if n % i == 0:
            count += 2

    return count


def find_triangle_number(count: int) -> int:
    """
    function:To find the triangle number that has number of divisors more than count
    params: count of type int
    returns: triangle number of type int
    """
    n = curr = 1

    while curr <= count:
        res = get_triangle_number(n)
        curr = no_of_divisors(res)
        n += 1

    return res


print(find_triangle_number(500))
