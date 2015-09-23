# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 19:48:28 2015

@author: simonfredon
"""

import json

with open("example.json") as json_file:
    json_data = json.load(json_file)
    print(json_data)