# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:45:04 2015

@author: simonfredon
"""

import sys

for arg in sys.argv[1:]:
    try:
        print(sys.argv[1])
    except IOError:
        print("Not enough parameters.")
