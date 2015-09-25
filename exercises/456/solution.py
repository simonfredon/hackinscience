# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:35:35 2015

@author: simonfredon
"""

import itertools
from master_mind import *


def solve_mind(x, code):
    tries = list(itertools.combinations_with_replacement(x, len(code)))
    for i in tries:
        puttana = []
        for j in i:
            puttana.append(j)
        i = puttana
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
