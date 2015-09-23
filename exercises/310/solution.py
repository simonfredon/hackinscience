# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:54:46 2015

@author: pippo
"""

inpy = open("words.txt", "r")
inprint = inpy.read()
count = 0
for i in inprint:
    if i == "e":
        count += 1
inpy.close()

print(count)
