# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:59:37 2015

@author: simonfredon
"""

import isprime
a = 0

for i in range(2, 1000):
    if isprime.is_prime(i):
        a += i

print(a)
