# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 12:12:49 2015

@author: simonfredon
"""

import requests

try:
    r = requests.get('http://mdk.fr/ip')
    test = r.text.split('\n')
    print(test[0])
except:
    print('No internet connectivity.')
