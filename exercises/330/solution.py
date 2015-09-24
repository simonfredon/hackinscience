# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 19:48:28 2015

@author: simonfredon
"""

import json


def load_json(x):
    with open(x) as xx:
        l = json.load(xx)
    return l
