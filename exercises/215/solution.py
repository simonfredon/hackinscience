# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:50:28 2015

@author: simonfredon
"""

import isprime

from numpy import binary_repr

for i in range(222281, 222381):
    x = binary_repr(i)
    if isprime.is_prime(x):
        print(i) 

