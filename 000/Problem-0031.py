"""
In England, the currency is made up of pound (£)
and pence (p). There are eight coins in general
circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can £2 be made using any
number of coins?
"""


def count_coin_combinations(target, coins):
    combinations = [1] + [0] * target

    for coin in coins:
        for value in range(coin, target + 1):
            combinations[value] += combinations[value - coin]

    return combinations[target]


print(count_coin_combinations(200, [1, 2, 5, 10, 20, 50, 100, 200]))
