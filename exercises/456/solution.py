# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:35:35 2015

@author: simonfredon
"""

import itertools
from master_mind import *
code = ""
colors = ""


def gen_colors(x):
    if x in range(0, 26):
        return alpha[:x]
    else:
        return alpha


def gen_code(x, alpha):
    return ''.join(random.choice(alpha[:x]) for i in range(x))


def solve_mind(x, y):
    tries = list(itertools.combinations_with_replacement(x, len(y)))
    for i in tries:
        i = "".join(i)
    for j in range(0, len(tries)):
        a = random.choice(tries)
        if a == code:
            return (a, j)
        else:
            culo = score_guess(a, code)
            for i in tries:
                vaffan = score_guess(i, code)
                if vaffan == culo:
                    tries.remove(i)
