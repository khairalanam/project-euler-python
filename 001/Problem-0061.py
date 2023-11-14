from itertools import permutations


def generate_figurates(s, start, end):
    figurates = []
    n = 1
    while True:
        value = s(n)
        if value > end:
            break
        if value >= start:
            figurates.append(value)
        n += 1
    return figurates


def find_cyclic_set():
    functions = [
        lambda n: n * (n + 1) // 2,
        lambda n: n * n,
        lambda n: n * (3 * n - 1) // 2,
        lambda n: n * (2 * n - 1),
        lambda n: n * (5 * n - 3) // 2,
        lambda n: n * (3 * n - 2)
    ]

    for perm in permutations(range(6)):
        for t in generate_figurates(functions[perm[0]], 1000, 9999):
            seq = [t]
            for i in range(1, 6):
                found = False
                for f in generate_figurates(functions[perm[i]], 1000, 9999):
                    if str(t)[-2:] == str(f)[:2] and f not in seq:
                        seq.append(f)
                        t = f
                        found = True
                        break
                if not found:
                    break
            if len(seq) == 6 and str(seq[-1])[2:] == str(seq[0])[:2]:
                return seq


print(sum(find_cyclic_set()))
