from itertools import permutations


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


def find_prime_permutation_sequence():
    for n in range(1000, 10000):
        if n != 1487 and is_prime(n):
            for diff in range(2, (10000 - n) // 2 + 1):
                b = n + diff
                c = n + 2 * diff

                if is_prime(b) and is_prime(c):
                    perms = [''.join(p) for p in permutations(str(n))]
                    if str(b) in perms and str(c) in perms:
                        if n != 1487:
                            return str(n) + str(b) + str(c)


print(find_prime_permutation_sequence())
