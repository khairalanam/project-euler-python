from collections import defaultdict


def find_cubic_permutations():
    cubes = defaultdict(list)

    n = 1
    while True:
        cube = n * n * n
        key = ''.join(sorted(str(cube)))
        cubes[key].append(cube)

        if len(cubes[key]) == 5:
            return cubes[key]

        n += 1


print(min(find_cubic_permutations()))
