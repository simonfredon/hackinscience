# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:22:14 2015

@author: simonfredon
"""

import json

json1_file = open("velib.json", encoding="utf-8")
json1_str = json1_file.read()

l = json.loads(json1_str)

errors = []
for i in range(len(l)):
    try:
        l[i]["city"] = l[i]["address"].split(" - ")[1].split(" ")[1]
        l[i]["zip_code"] = l[i]["address"].split(" - ")[1].split(" ")[0]
        l[i]["address"] = l[i]["address"].split(" - ")[0]
        l[i]["name"] = l[i]["name"].split(" - ")[1]
    except:
        errors.append(i)

errors2 = []
for i in errors:
    try:
        l[i]["city"] = l[i]["address"].split("- ")[1].split(" ")[1]
        l[i]["zip_code"] = l[i]["address"].split("- ")[1].split(" ")[0]
        l[i]["address"] = l[i]["address"].split("- ")[0]
        l[i]["name"] = l[i]["name"].split(" - ")[1]
    except:
        errors2.append(i)

errors3 = []
for i in errors2:
    try:
            l[i]["city"] = l[i]["address"].split()[-1]
            l[i]["zip_code"] = l[i]["address"].split()[-2]
            k = l[i]["address"].split()[:-2]
            l[i]["address"] = " ".join(k)
            l[i]["name"] = l[i]["name"].split(" - ")[1]
    except:
        errors3.append(i)

solution = json.dumps(l)

with open('solution.json', 'w') as outfile:
    json.dump(l, outfile)
