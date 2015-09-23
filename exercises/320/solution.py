# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:54:46 2015

@author: pippo
"""
import string
alphy = list(string.ascii_lowercase)
print(alphy)
inpy = open("words.txt", "r")
inprint = inpy.read()
lungo = len (inprint)
count = [0] * 26
for j in range(0, 26):
    for i in inprint:
        if i == alphy[j]:
            count[j] += 1
inpy.close()

for j in range(0, 26):
    print(alphy[j] + ':', count[j] / lungo)
