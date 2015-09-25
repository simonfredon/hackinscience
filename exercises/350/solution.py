# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 12:07:22 2015

@author: simonfredon
"""

import bencode_tools as bt


def encode(stuff):
    return bytes(bt.encode2(stuff), encoding='ascii')
