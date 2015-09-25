# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:35:35 2015

@author: simonfredon
"""
import string
import itertools
from master_mind import *

colors = ""
code = ""

def gen_colors(x):
    if x in range(0, 26):
        return alpha[:x]
    else:
        return alpha


def gen_code(x, alpha):
    return ''.join(random.choice(alpha[:x]) for i in range(x))


def solve_mind(x, y):
    return (x, 2)
    
    