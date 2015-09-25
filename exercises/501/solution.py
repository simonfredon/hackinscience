# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 12:06:47 2015

@author: simonfredon
"""


def best_change(amout, coins):
    change = []
    if amout <= coins[-1]:
        return None
    for i in coins:
        if i < amout:
            change.append(i)
            amout = amout - i
            break
    while amout != 0:
        for i in coins:
            if i <= amout:
                change.append(i)
                amout = amout - i
                break
    return change


def changes(amout, coins):
    coins = tuple(sorted(coins, reverse=True))
    count = 1
    count_init = 0
    change = [amout]
    while count_init != count:
        # print(change)
        # print(count)
        count_init = count
        for i in reversed(range(0, len(change))):
            X = best_change(change[i], coins)
            if X is not None:
                count = count + 1
                del change[i]
                for j in X:
                    change.append(j)
                break
        change = sorted(change, reverse=True)
    return count
