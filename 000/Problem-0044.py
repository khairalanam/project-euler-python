def is_pentagonal(n):
    discriminant = 1 + 24 * n
    sqrt_discriminant = int(discriminant**0.5)
    return sqrt_discriminant**2 == discriminant and (sqrt_discriminant + 1) % 6 == 0


def find_minimized_pentagonal_difference():
    pentagonals = set()
    j = 1

    while True:
        pent_j = j * (3 * j - 1) // 2
        for pent_k in pentagonals:
            if is_pentagonal(pent_j - pent_k) and is_pentagonal(pent_j + pent_k):
                return pent_j - pent_k
        pentagonals.add(pent_j)
        j += 1


print(find_minimized_pentagonal_difference())
