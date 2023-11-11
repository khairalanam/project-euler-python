def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def count_primes_ratio():
    side_length = total_numbers = 1
    primes_count = 0

    while True:
        side_length += 2
        for i in range(4):
            diagonal_number = side_length ** 2 - i * (side_length - 1)
            if is_prime(diagonal_number):
                primes_count += 1

        total_numbers += 4

        ratio = primes_count / total_numbers
        if ratio < 0.1:
            return side_length


print(count_primes_ratio())
