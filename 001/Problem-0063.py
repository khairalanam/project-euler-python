def count_n_digit_powers(n):
    count = 0
    for i in range(1, 10):
        power = 1
        while len(str(i ** power)) == power:
            count += 1
            power += 1
    return count


result = count_n_digit_powers(100)
print(result)
