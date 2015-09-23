# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:15:38 2015

@author: simonfredon
"""


def starts_with(alpha, top):
    alphalist = list(alpha)
    toplist = list(top)
    if len(alphalist) < len(toplist):
        return False
    for i in range(1, len(toplist)):
        if alphalist[i] not in toplist[i]:
            return False
    return True
