#!/usr/bin/python3
""" Making-change
"""


def makeChange(coins, total):
    """Determine the fewest number of coins needed
    to meet a given amount total
    """
    if total <= 0:
        return 0
    R = total
    coinsCount = 0
    coinIdx = 0
    sortedCoins = sorted(coins, reverse=True)
    l = len(coins)
    while R > 0:
        if coinIdx >= l:
            return -1
        if R - sortedCoins[coinIdx] >= 0:
            R -= sortedCoins[coinIdx]
            coinsCount += 1
        else:
            coinIdx += 1
    return coinsCount
