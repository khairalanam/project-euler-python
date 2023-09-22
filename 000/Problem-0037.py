"""
The number 3797 has an interesting property.
Being prime itself, it is possible to continuously
remove digits from left to right, and remain prime
at each stage: 3797, 797, 97, and 7.
Similarly, we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only n (e.g., 11) primes
that are both truncatable from left to right
and right to left.

Note: 2, 3, 5, and 7 are not considered truncatable primes.
"""


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_truncatable_prime(n):
    if n < 10:
        return False

    num_str = str(n)
    num_len = len(num_str)

    for i in range(num_len):
        left_truncated = int(num_str[i:])
        right_truncated = int(num_str[:num_len - i])
        if not is_prime(left_truncated) or not is_prime(right_truncated):
            return False
    return True


def find_truncatable_primes(count):
    truncatable_primes = []
    num = 10

    while len(truncatable_primes) < count:
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
        num += 1

    return truncatable_primes


print(sum(find_truncatable_primes(11)))
