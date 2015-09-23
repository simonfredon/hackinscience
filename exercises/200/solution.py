# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:31:30 2015

@author: simonfredon
"""


def is_prime(num):
    if num == 1:
        return False
    n = num ** 0.5
    for i in list(range(2, (int(n) + 1))):
        if num % i == 0:
            return False
    return True
