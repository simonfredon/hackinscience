# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:50:28 2015

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


def dec2bin(d,nb=0):
    if d==0:
        b="0"
    else:
        b=""
        while d!=0:
            b="01"[d&1]+b
            d=d>>1
    return b.zfill(nb)

for i in range(222281, 222381):
    x = dec2bin(i)
    if is_prime(x):
        print(i) 
