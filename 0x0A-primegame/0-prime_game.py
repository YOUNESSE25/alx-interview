#!/usr/bin/python3
"""
0. Prime Game
"""


def Prim(n):
    """
    Prime numbers between 1 and n inclusive
    """
    prim = []
    siev = [True] * (n + 1)
    for p in range(2, n + 1):
        if (siev[p]):
            prim.append(p)
            for i in range(p, n + 1, p):
                siev[i] = False
    return prim


def isWinner(x, nums):
    """
    Winner of Prime Game
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    M = B = 0
    for i in range(x):
        prime = Prim(nums[i])
        if len(prime) % 2 == 0:
            B += 1
        else:
            M += 1
    if M > B:
        return 'Maria'
    elif B > M:
        return 'Ben'
    return None
