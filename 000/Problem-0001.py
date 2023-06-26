def sum_of_three_or_five(n):
    res = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            res += i

    return res

print(sum_of_three_or_five(1000))