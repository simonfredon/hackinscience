# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:22:50 2015

@author: simonfredon
"""

import sys

if len(sys.argv) > 2:
    print(int(sys.argv[1]) + int(sys.argv[2]))
else:
    print("usage: python3 solution.py OP1 OP2")
