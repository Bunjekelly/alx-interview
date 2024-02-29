#!/usr/bin/python3

"""a function that determine the fewest number
of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """Return the minimum number of coins needed to meet a given total"""
    dp = [float('inf')] * (total + 1)

    dp[0] = 0

    for coin in coins:
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]
