# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:31:30 2015

@author: simonfredon
"""


def is_prime(num):
    x = True
    n = num ** 0.5
    if num == 0:
        return x == False
    for i in range(2, int(n + 1)):
        if num % i == 0:
            return x == False
        else:
            return x == True
