""""
Each new term in the Fibonacci sequence is generated
by adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89.

Problem: By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms.
"""

def sum_even_fibonacci(limit):
    first = 1

    # initially assign res = 2 since we add only even fibonacci numbers
    second = res = 2
    final = 0

    # the loop continues until the current fibonacci number reaches/exceeds the limit
    while final < limit:
        final = first + second
        first, second = second, final

        # Add only even fibonacci numbers to the final result
        if final % 2 == 0:
            res += final

    return res

print(sum_even_fibonacci(4000000))