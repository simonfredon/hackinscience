# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:54:46 2015

@author: pippo
"""
import string
alph = list(string.ascii_lowercase)
print(alph)
inpy = open("words.txt", "r")
inprint = inpy.read()
long = len(inprint)
count = [0] * 26
for j in range(0, 26):
    for i in inprint:
        if i == alph[j]:
            count[j] += 1
inpy.close()

for j in range(0, 26):
    print(alph[j] + ':', count[j] / long)
