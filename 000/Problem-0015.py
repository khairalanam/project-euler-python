"""
Starting in the top left corner of a 2 x 2 grid,
and only being able to move to the right and down,
there are exactly routes to the bottom right corner.

Problem: How many such routes are there through a 20 x 20 grid?
"""

"""
Logic: This is almost the same as the Unique Paths problem
from Leetcode.

Just use dynamic programming.

There's only one tricky part, the path is along the edges and
not the actual cells. This implies for n x n grid, you have
to implement Unique Paths problem algorithm for n + 1 x n + 1
grid.
"""

def unique_paths(m, n, dp={}, flag=False):
    """
    function: To find the unique paths along the edges of an m x n grid
    params: grid dimensions m and n of type int, dp dicitonary for memo, and flag
    to make sure we are counting n + 1 and not n.
    """
    if not flag:
        m += 1
        n += 1
        flag = True
    if m == 1 or n == 1:
        dp[(m, n)] = 1
        return dp[(m, n)]

    if (m, n) in dp:
        return dp[(m, n)]

    dp[(m, n)] = unique_paths(m - 1, n, dp, flag) + unique_paths(m, n - 1, dp, flag)
    return dp[(m, n)]

print(unique_paths(20, 20))