# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:09:48 2015

@author: pippo
"""
import string
import checker
al = list(string.ascii_lowercase)
AL = list(string.ascii_uppercase)
forward = "forward"
backward = "backward"


def caesar_cypher(s, k, m):
    code = list(s)
    ori = list(s)
    resu = list(s)
    for i in range(0, len(s)):
        if checker.numa(ori[i]) != 666:
            if checker.numa(ori[i]) % 1 == 0:
                code[i] = checker.numa(ori[i])
                if m == "backward":
                    code[i] = (code[i] - k) % 26
                if m == "forward":
                    code[i] = (code[i] + k) % 26
                resu[i] = al[code[i]]
            if checker.numa(ori[i]) % 1 == 0.5:
                code[i] = int(checker.numa(ori[i]) - 0.5)
                if m == "backward":
                    code[i] = (code[i] - k) % 26
                if m == "forward":
                    code[i] = (code[i] + k) % 26
                resu[i] = AL[code[i]]
        else:
            resu[i] = ori[i]
    return ''.join(resu)
