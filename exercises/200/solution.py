# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:31:30 2015

@author: simonfredon
"""


def is_prime(num):
    n = num ** 0.5
    if num == 0:
        return False
    for i in range(2, int(n + 1)):
        if num % i == 0:
            return False
        else:
            return True
