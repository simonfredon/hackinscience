# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:15:34 2015

@author: simonfredon
"""

import sys

command = ['+', '-', '*', '/', '%', '^']

if len(sys.argv) == 4:
    b = sys.argv[2]
    try:
        a = int(sys.argv[1])
        c = int(sys.argv[3])
        if b in command:
            if b == '+':
                d = a + c
            elif b == '-':
                d = a - c
            elif b == '*':
                d = a * c
            elif b == '/':
                d = a / c
            elif b == '%':
                d = a % c
            elif b == '^':
                d = a ** c
            print(d)
        else:
            print('input error')
    except:
        print("input error")
else:
    print('usage: ./solution.py a_number (an_operator +-*/%^) a_number')
