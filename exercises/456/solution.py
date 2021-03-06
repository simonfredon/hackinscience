# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:35:35 2015

@author: simonfredon
"""

import itertools
from master_mind import *


def solve_mind(x, code):
#    tries = [''.join(x) for x in
#             itertools.combinations_with_replacement(x, len(code))]
    tries = [''.join(x) for x in list(itertools.product(x, repeat=len(code)))]
    print(tries)
    guess_count = 1
    while True:
        guess = tries.pop(random.randint(0, len(tries) - 1))
        score = score_guess(guess, code)
        if score == (4, 0):
            return (guess, guess_count)
        tries = [x for x in
                 tries if score_guess(x, code) == score]
        guess_count += 1


#    for i in tries:
#        puttana = ""
#        for j in i:
#            puttana = puttana + j
#        tries2.append(puttana)
#    tries = tries2
#    for j in range(0, len(tries)):
#        a = random.choice(tries)
#        print(a)
#        if a == code:
#            return (a, j)
#        else:
#            culo = score_guess(a, code)
#            for i in tries:
#                vaffan = score_guess(i, code)
#                if vaffan == culo:
#                    tries.remove(i)
