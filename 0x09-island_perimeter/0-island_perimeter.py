#!/usr/bin/python3

"""a function def island_perimeter(grid): that returns
the perimeter of the island described in grid"""

def island_perimeter(grid):
    """a function def island_perimeter(grid): that returns
    the perimeter of the island described in grid"""
    rows = len(grid)
    columns = len(grid[0])

    result = 0

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 1:
                if c == 0 or grid[r][c-1] == 0:
                    result += 1

                if c == columns-1 or grid[r][c+1] == 0:
                    result += 1

                if r == 0 or grid[r-1][c] == 0:
                    result += 1

                if r == rows-1 or grid[r+1][c] == 0:
                    result += 1

    return result
