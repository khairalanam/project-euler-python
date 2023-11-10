from fractions import Fraction


def expansion(n):
    frac = Fraction(1, 1)

    for _ in range(n):
        frac = 1 + 1 / (1 + frac)

    return frac


def count_expansions(iterations):
    count = 0
    for i in range(iterations):
        frac = expansion(i)
        if len(str(frac.numerator)) > len(str(frac.denominator)):
            count += 1

    return count


print(count_expansions(1000))
