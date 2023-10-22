from collections import Counter


def sieve(n):
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, int(n**0.5 + 1), 2):
        index = i * 2
        while index < n:
            is_prime[index] = False
            index = index + i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime


primes = sieve(1000000)

primes = [x for x in primes if len(str(x)) - len(set(str(x))) >= 3]


def pdr(s):
    s = str(s)
    sol = []
    for duplicate in (Counter(s) - Counter(set(s))):
        temp = [int(s.replace(duplicate, x)) for x in '0123456789']
        sol.append(temp)
    return sol


checked = []


def check(l):
    for i in l:
        checked.append(i)
        if i not in primes:
            l.remove(i)
    return l


flag = True
i = 0

while flag:
    if primes[i] not in checked:
        replacements = pdr(primes[i])
        for j in replacements:
            if len(check(j)) == 8:
                print(j[0])
                flag = False
                break
    i += 1
