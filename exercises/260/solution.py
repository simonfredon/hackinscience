# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:42:40 2015

@author: simonfredon
"""

import math
import numpy as np


def euclidean(a, b):
    d = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5
    return d


def opt_euclidean(a, b):
    d2 = math.pow(math.pow(b[0] - a[0], 2) + math.pow(b[1] - a[1], 2), 0.5)
    return d2


a = np.array(())
b = np.array(())

def np_euclidean(a, b):
    d3 = np.linalg.norm(a-b)
    return d3
