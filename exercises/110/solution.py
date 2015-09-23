# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:15:34 2015

@author: simonfredon
"""

import sys

command = ['+', '-', '\*', '//', '%', '^']

if len(sys.argv) > 3:
    def op(a, b, c):
        if isinstance(a, int):
            if isinstance(c, int):
                if b in command:
                    if b == '+':
                        d = a + b
                    elif b == '-':
                        d = a - b
                    elif b == '\*':
                        d = a * b
                    elif b == '//':
                        d = a / b
                    elif b == '%':
                        d = a % b
                    else:
                        d = a ** b
                    print(d)
                else:
                    print('input error')
            else:
                print('input error')
        else:
            print('input error')
else:
    print('usage: ./solution.py a_number (an_operator +-*/%^) a_number')
