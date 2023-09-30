from itertools import permutations


def has_substring_divisibility_property(number_str):
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        sub_number = int(number_str[i:i+3])
        if sub_number % primes[i-1] != 0:
            return False
    return True


pandigital_numbers = [''.join(p)
                      for p in permutations("0123456789") if p[0] != '0']
result = sum(int(num)
             for num in pandigital_numbers if has_substring_divisibility_property(num))

print(result)
