# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:47:40 2015

@author: simonfredon
"""


def love_meet(a, b):
    meet = a.intersection(b)
    return meet


def affair_meet(b, a, c):
    meet = a.intersection(c)
    unmeet = meet.difference(b)
    return unmeet
