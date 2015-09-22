# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:11:48 2015

@author: simonfredon
"""

a = 0
for i in range(0, 1001):
    if i % 3 == 0:
        a += i
    if i % 5 ==0:
        a += i
print(a)
