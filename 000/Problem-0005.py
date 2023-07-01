"""
2520 is the smallest number that can be divided by each of
the numbers from 1 to 10 without any remainder

Problem: What is the smallest positive number that is evenly
divisble by all of the numbers from 1 to 20.
"""

def gcd(a: int, b: int) -> int:
    """
    function: To find greatest common divisor of two integers a and b
    params: a: int, b: int
    """
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """
    function: To find the least common multiple of two integers a and b
    params: a: int, b: int

    property: a * b = lcm(a, b) * gcd(a, b)
    """
    return (a * b) // gcd(a, b)

def smallest_product(start, end):
    res = 1

    for i in range(start, end + 1):

        # res % i will ensure that repetitive factors are not multiplied to the result
        if res % i:
            res = lcm(res, i)

    return res

print(smallest_product(1, 20))