def self_powers_last_ten_digits(limit):
    result = 0
    for n in range(1, limit + 1):
        result += n ** n
    return str(result)[-10:]


print(self_powers_last_ten_digits(1000))
