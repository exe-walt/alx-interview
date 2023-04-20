#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
"""
         returns a list of lists of
         integers representing
          the Pascal’s triangle of n
         Returns an empty list if n <= 0
 """
 triangle = []
    if n <= 0:
        triangle
    else:
        for i in range(n):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
    return triangle
