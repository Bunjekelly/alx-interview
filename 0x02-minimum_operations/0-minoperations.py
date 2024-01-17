#!/usr/bin/python3

""" a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file"""

def minOperations(n):
    """function definition"""
    if n < 2:
        return 0

    result = 0

    for i in range(2, n + 1):
        while n % i == 0:
            result += i
            n = n // i

        if n == 1:
            break

    return result
