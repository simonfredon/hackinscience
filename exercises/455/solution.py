# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:16:21 2015

@author: simonfredon
"""

import string
import random

alpha = string.ascii_uppercase


def gen_colors(x):
    if x in range(0, 26):
        return alpha[:x]
    else:
        return alpha


def gen_code(x, alpha):
    return ''.join(random.choice(alpha[:x]) for i in range(x))

guess = ""


def check_guess(guess, x, alpha):
    if len(gen_code(x, alpha)) == len(guess):
        if guess in alpha[:x]:
            return True
    return False


def score_guess(guess, gen_code):
    count1 = 0
    count2 = 0
    for i, j in zip(guess, gen_code):
        if i == j:
                count1 += 1
                gen_code = gen_code.replace(j, "0", 1)
                print(gen_code)
        elif i in gen_code:
                count2 += 1
                gen_code = gen_code.replace(i, "0", 1)
                print(gen_code)
    return (count1, count2)
