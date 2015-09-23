# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:18:49 2015

@author: simonfredon
"""


def is_multiple(a):
    b = int(len(a) / 2)
    c = [0] * len(a)
    for i in range(0, b):
        c[(i * 2)] = a[i]
        c[(i * 2) + 1] = a[i + (b)]
    return c
