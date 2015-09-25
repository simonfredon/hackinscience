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
    tries = list(itertools.combinations_with_replacement(list(y), x))
    for i in tries:
        i = "".join(i)
    for j in range(0, len(tries)):
        a = random.choice(tries)
        if a == code:
            return (a, j)
        else:
            culo = master_mind.score_guess(a, code)
            for i in tries:
                vaffan = master_mind.score_guess(i, code)
                if vaffan == culo:
                    tries.remove(i)
