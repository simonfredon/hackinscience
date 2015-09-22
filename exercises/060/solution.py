# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:27:28 2015

@author: simonfredon
"""

word = "abcdefghijklmnopqrstuvwxyz"

for i in range(0, 26):
    for j in range(0, 26):
        print(word[i] + word[j])
