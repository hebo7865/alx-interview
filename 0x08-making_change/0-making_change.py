#!/usr/bin/python3
""" making change"""


def makeChange(coins, total):
    """ Given a list of coin denominations and a total, return the fewest
    """
    if total < 1:
        return 0
    coins.sort()
    coins.reverse()
    few = 0
    for coin in coins:
        if total <= 0:
            break
        buff = total // coin
        few += buff
        total -= (buff * coin)
    if total != 0:
        return -1
    return few
