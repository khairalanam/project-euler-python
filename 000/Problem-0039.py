"""
If p is the perimeter of a right angle triangle with
integral length sides, {a,b,c}, there are exactly
three solutions for p = 120:

    {20,48,52}, 20^2 + 48^2 = 52^2
    {24,45,51}, 24^2 + 45^2 = 51^2
    {30,40,50}, 30^2 + 40^2 = 50^2

For which value of p <= 1000, is the number of solutions maximized?
"""


def count_right_triangles(p):
    count = 0

    for a in range(1, p // 2):
        for b in range(a, p // 2):
            c = p - a - b
            if a * a + b * b == c * c:
                count += 1

    return count


def find_maximum_solutions_perimeter(limit):
    max_solutions = max_solutions_perimeter = 0

    for p in range(3, limit + 1):
        solutions = count_right_triangles(p)
        if solutions > max_solutions:
            max_solutions = solutions
            max_solutions_perimeter = p

    return max_solutions_perimeter


print(find_maximum_solutions_perimeter(1000))
