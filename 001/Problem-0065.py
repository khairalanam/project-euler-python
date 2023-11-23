from fractions import Fraction


def e_sequence(n):
    sequence = [2]
    for k in range(1, n + 1):
        sequence.extend([1, 2 * k, 1])
    return sequence[: n]


def nth_convergent_e(n):
    sequence = e_sequence(n)
    fraction = Fraction(sequence[-1])
    for i in reversed(sequence[: -1]):
        fraction = i + Fraction(1, fraction)
    return fraction


def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))


convergent = nth_convergent_e(100)
print(sum_of_digits(convergent.numerator))
