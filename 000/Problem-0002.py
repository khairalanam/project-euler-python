def sum_even_fibonacci(limit):
    first = 1
    second = res = 2
    flag = False
    final = 0

    while final < limit:
        final = first + second
        first, second = second, final

        if final % 2 == 0:
            res += final

    return res

print(sum_even_fibonacci(4000000))