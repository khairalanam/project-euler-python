def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(limit ** 0.5) + 1):
        if sieve[p]:
            for multiple in range(p * p, limit + 1, p):
                sieve[multiple] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]


def find_longest_consecutive_prime_sum(limit):
    primes = sieve_of_eratosthenes(limit)
    max_length = max_prime = 0

    for i in range(len(primes)):
        for j in range(i + max_length, len(primes)):
            prime_sum = sum(primes[i: j])
            if prime_sum < limit and prime_sum in primes:
                if j - i > max_length:
                    max_length = j - i
                    max_prime = prime_sum
            elif prime_sum >= limit:
                break

    return max_prime


print(find_longest_consecutive_prime_sum(1000000))
