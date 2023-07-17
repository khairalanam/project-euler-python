"""
The following iterative sequence is defined for the set of positive integers:

n -> n / 2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting from 13
and finishing at 1) contains 10 terms. Although it has
not been proven yet (Collatz Problem), it is thought that
all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""


def collatz_sequence_length(n: int, cache: dict = {}) -> int:
    """
    function: To find the number of terms in the collatz sequence of a given number n
    params: numbe rn of type int and cache of type dictionary
    returns: number of terms of type int
    """
    if n in cache:
        return cache[n]

    if n == 1:
        return 1

    if n % 2 == 0:
        length = 1 + collatz_sequence_length(n // 2, cache)
    else:
        length = 1 + collatz_sequence_length(3 * n + 1, cache)

    cache[n] = length
    return cache[n]


def find_longest_collatz_sequence(limit: int) -> int:
    """
    function: To find the longest collatz sequence with the given limit
    params: limit of type int
    returns: the starting number with the longest collatz sequence under the given limit
    """
    max_length = max_starting_number = 0

    for i in range(limit - 1, 0, -1):
        length = collatz_sequence_length(i)
        if length > max_length:
            max_length = length
            max_starting_number = i

    return max_starting_number


print(find_longest_collatz_sequence(1000000))
