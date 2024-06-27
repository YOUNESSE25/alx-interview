#!/usr/bin/python3
"""
returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """pascal_triangle"""
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for k in range(n):
        NewRow = [0] * (k+1)
        NewRow[0] = 1
        NewRow[len(NewRow) - 1] = 1

        for l in range(1, k):
            if l > 0 and l < len(NewRow):
                a = pascal_triangle[k - 1][l]
                b = pascal_triangle[k - 1][l - 1]
                NewRow[l] = a + b

        pascal_triangle[k] = NewRow

    return pascal_triangle
