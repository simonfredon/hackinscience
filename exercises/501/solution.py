# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 12:06:47 2015

@author: simonfredon
"""


def changes(amount, coins_rv):
    count = 0
    while coins_rv[0] > amount:
        del coins_rv[0]
    maxi = amount // coins_rv[0]
    for i in reversed(range(0, maxi + 1)):
        rest = amount - i * coins_rv[0]
        if rest == 0:
            count = count + 1
        else:
            if len(coins_rv) > 1:
                count = count + changes(rest, coins_rv[1:])
    return count
