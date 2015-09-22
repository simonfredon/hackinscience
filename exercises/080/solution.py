# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:02:51 2015

@author: simonfredon
"""

import string

a = string.ascii_lowercase

b = 1
for i in range(0, 25):
    for j in range(b, 26):
        print(a[i] + a[j])
b = b + 1
