# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 12:03:25 2015

@author: simonfredon
"""

import isprime

s = ""
for i in range(10000, 100050):
    if isprime.is_prime(i):
        s += str(str(i) + ', ')
s[:-2]
print(s)
