# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:31:30 2015

@author: simonfredon
"""


def is_prime(num):
    check = 0
    x = True
    for i in range(2, num - 1):
        if num % i == 0:
            check += 1
    if check > 0:
        x = False
    else:
        x = True
    if num == 1:
        x = False
    return x
