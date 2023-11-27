with open('triangle.txt') as file:
    triangle = [[int(num) for num in line.split()] for line in file]


def find_maximum_path_sum(triangle):
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    return triangle[0][0]


print(find_maximum_path_sum(triangle))
