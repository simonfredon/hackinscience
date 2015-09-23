# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:05:12 2015

@author: simonfredon
"""

from operator import *


def select_student(l, tr):
    a = len(l)
    acc = list()
    ref = list()
    for i in range(0, a):
        if l[i][1] >= tr:
            acc.append(l[i])
        else:
            ref.append(l[i])
    res = {'Accepted': sorted(acc, key=itemgetter(1), reverse=True),
           'Refused': sorted(ref, key=itemgetter(1))}
    return res
