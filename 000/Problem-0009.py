"""
A Pythagorean triplet is a set of three natural numbers, a < b < c,
for which, a^2 + b^2 = c^2.

For example, (3^2) + (4^2) = 9 + 16 = 25 = (5^2).

Problem: There exists exactly one Pythagorean triplet
for which a + b + c = 1000.
Find the product abc.
"""

def find_triplet(limit) -> tuple[int]:
    """
    function: find the Pythagorean triplet in which a + b + c = limit
    params: limit of type int
    returns: Pythagorean triplet of type tuple[int] if found else an empty tuple
    """

    # A special property of Pythagorean triplet
    # for a Pythagorean triplet a, b, c and two integers m, n where m > n
    # a = m ^ 2 - n ^ 2
    # b = 2 * m * n
    # c = m ^ 2 + n ^ 2

    m = 2
    n = 1

    while (m, n) != (limit, limit - 1):
        m_square = m * m
        n_square = n * n
        a = m_square - n_square
        b = 2 * m * n
        c = m_square + n_square

        if a + b + c == limit:
            return a, b, c

        if m == limit:
            n += 1
            m = n

        m += 1

    return ()

a, b, c = find_triplet(1000)
print(a * b * c)