#!/usr/bin/env python3

"""a function def pascal_triangle(n): that returns a list of lists
of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """function definition"""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[-1]
        row += [last_row[j] + last_row[j+1] for j in range(len(last_row) - 1)]
        row.append(1)
        triangle.append(row)
    return triangle
