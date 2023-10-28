def has_same_digits(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))


def find_smallest_permuted_multiple():
    x = 1
    while True:
        if all(has_same_digits(x, x * i) for i in range(2, 7)):
            return x
        x += 1


print(find_smallest_permuted_multiple())
