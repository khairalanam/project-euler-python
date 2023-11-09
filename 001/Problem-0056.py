def digit_sum(n):
    return sum(int(digit) for digit in str(n))


max_sum = 0
main_range = range(1, 100)

for a in main_range:
    for b in main_range:
        power_sum = digit_sum(a ** b)
        if power_sum > max_sum:
            max_sum = power_sum

print(max_sum)
