#!/usr/bin/python3
'''Minimum Operations python3 challenge'''


def minOperations(n):
    '''
    execute two operations in this file: Copy All and Paste. Given a number n,
    write a method that calculates the fewest number of operations needed to result
    in exactly n H characters in the file
    '''
    in_chars = 1
    cboard = 0
    count = 0

    while in_chars < n:
        if cboard == 0:
            cboard = in_chars
            count += 1

        if in_chars == 1:
            in_chars += cboard
            count += 1
            continue

        remaining = n - in_chars
        if remaining < cboard:
            return 0

        if remaining % in_chars != 0:
            in_chars += cboard
            count += 1
        else:
            cboard = in_chars
            in_chars += cboard
            count += 2

    if in_chars == n:
        return count
    else:
        return 0
