# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 18:57:35 2015

@author: simonfredon
"""

word = "abcdefghijklmnopqrstuvwxyz"

for i in range(0, 26):
    for j in range(0, 26):
        if i != j:
            print(word[i] + word[j])
