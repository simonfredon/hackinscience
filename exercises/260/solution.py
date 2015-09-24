# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:42:40 2015

@author: simonfredon
"""

import math
import numpy as nu


def euclidean(x, y):
    distance = 0
    for i in range(len(x)):
        distance = distance + (y[i] - x[i])**2
    distance_fin = distance**0.5
    return distance_fin


def opt_euclidean(x, y):
    k = 0
    for i in range(len(x)):
        k = k + math.pow(y[i] - x[i], 2)
    return math.pow(k, 0.5)


def np_euclidean(x, y):
    return nu.sqrt(nu.sum(nu.power(nu.array(x) - nu.array(y), 2)))
