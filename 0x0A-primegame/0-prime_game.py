#!/usr/bin/python3

""" a module that determine who the winner of each game is"""


def isWinner(x, nums):
    """determining who wins"""

    def sieve(n):
        """sieves numbers"""
        primes = [True for _ in range(n+1)]
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n+1, p):
                    primes[i] = False
            p += 1
        return [p for p in range(2, n) if primes[p]]

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        primes = sieve(n)
        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
