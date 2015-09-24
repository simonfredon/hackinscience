# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:42:40 2015

@author: simonfredon
"""

import math
import numpy


def euclidean(a, b):
    d = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5
    return d


def opt_euclidean(a, b):
    d2 = math.pow(math.pow(b[0] - a[0], 2) + math.pow(b[1] - a[1], 2), 0.5)
    return d2


def np_euclidean(a, b):
    d3 = numpy.power(numpy.power(b[0] - a[0], 2) +
         numpy.power(b[0] - a[0], 2), 0.5)
    return d3
