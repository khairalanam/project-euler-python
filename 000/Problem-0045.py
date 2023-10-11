def find_next_triangular_pentagonal_hexagonal():
    n = 144
    while True:
        hexagonal = n * (2 * n - 1)
        if is_pentagonal(hexagonal) and is_triangular(hexagonal):
            return hexagonal
        n += 1


def is_pentagonal(n):
    discriminant = 1 + 24 * n
    sqrt_discriminant = int(discriminant**0.5)
    return sqrt_discriminant**2 == discriminant and (sqrt_discriminant + 1) % 6 == 0


def is_triangular(n):
    discriminant = 1 + 8 * n
    sqrt_discriminant = int(discriminant**0.5)
    return sqrt_discriminant**2 == discriminant and (-sqrt_discriminant - 1) % 2 == 0


print(find_next_triangular_pentagonal_hexagonal())
