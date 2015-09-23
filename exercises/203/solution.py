# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:18:49 2015

@author: simonfredon
"""


def perfect_shuffle(a):
    la = int(len(a) / 2)
    fin = [0] * len(a)
    for i in range(0, la):
        fin[(i * 2)] = a[i]
        fin[(i * 2) + 1] = a[i + (la)]
    return fin
