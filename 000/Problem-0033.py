"""
The fraction 49/98 is a curious fraction,
as an inexperienced mathematician in attempting
to simplify it may incorrectly believe that 49/98
= 4/8, which is correct, is obtained by canceling
the 9s.

We shall consider fractions like, 30/50 = 3/5, to
be trivial examples.

There are exactly four non-trivial examples of this
type of fraction, less than one in value, and containing
two digits in the numerator and denominator.

Find the value of the denominator of the product of these
four fractions in their simplest form.
"""

from fractions import Fraction


def digit_canceling_fractions():
    product = 1

    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):
            if numerator % 10 == 0 and denominator % 10 == 0:
                continue

            num_str, den_str = str(numerator), str(denominator)

            for digit in num_str:
                if digit in den_str:
                    num_cancel = int(num_str.replace(digit, '', 1))
                    den_cancel = int(den_str.replace(digit, '', 1))

                    if num_cancel * denominator == numerator * den_cancel:
                        product *= Fraction(num_cancel, den_cancel)

    return product


print(digit_canceling_fractions().denominator)
