# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:10:42 2015

@author: simonfredon
"""

import string

def is_alpha(al):
    alphalist = list(al)
    for i in alphalist:
        if i not in list(string.ascii_letters):
            return False
    return True
