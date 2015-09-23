# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:45:50 2015

@author: simonfredon
"""

import sys

lista = list(enumerate(sys.argv))
a = len(lista)

for i in range(0, a):
    print(i, sys.argv[i])
