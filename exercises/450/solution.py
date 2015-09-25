# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 11:37:48 2015

@author: simonfredon
"""

from string import ascii_lowercase
forward = 1
backward = -1
ascii_lc = ascii_lowercase
d_ascii = ascii_lowercase + ascii_lowercase


def caesar_cypher(s, key, method):
    try:
        s_input = s.lower()
        o_s = []
        case = s.split()
        i_s = s_input.split()
        if (key > 26):
            ukey = key % 26
        else:
            ukey = key
        for i in range(len(i_s)):
            code = str()
            for k in range(len(i_s[i])):
                try:
                    if (ascii_lc.index(i_s[i][k]) >= 0):
                        if (i_s[i][k] == case[i][k]):
                            code = (code + d_ascii[ascii_lc.index(i_s[i][k]) +
                                    (ukey * method)])
                        else:
                            code = (code + d_ascii[ascii_lc.index(i_s[i][k]) +
                                    (ukey * method)].upper())
                except Exception:
                    code = code + i_s[i][k]
            o_s.append(code)
        return ' '.join(str(e) for e in o_s)
    except Exception:
        return 'Input error'
