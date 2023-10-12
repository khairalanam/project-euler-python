import math


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def find_smallest_non_goldbach_odd_composite():
    n = 9
    while True:
        if not is_prime(n):
            found = False
            for prime in range(2, n):
                if is_prime(prime):
                    difference = n - prime
                    if difference % 2 == 0:
                        square = difference >> 1
                        root = int(math.sqrt(square))
                        if root * root == square:
                            found = True
                            break
            if not found:
                return n
        n += 2


print(find_smallest_non_goldbach_odd_composite())
