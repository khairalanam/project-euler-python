def is_palindrome(num):
    return str(num) == str(num)[::-1]


def is_lychrel(n, max_iterations=50):
    for _ in range(max_iterations):
        n += int(str(n)[::-1])
        if is_palindrome(n):
            return False
    return True


count = 0
for number in range(10, 10000):
    if is_lychrel(number):
        count += 1

print(count)
