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
        print(alpha[:x])
    else:
        print(alpha)


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
    for i in range(guess):
        if guess[i] == gen_code[i]:
            count1 = count1 + 1
        else:
            if guess[i] in gen_code:
                count2 = count2 + 1
    return (count1, count2)


        