# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 12:07:22 2015

@author: simonfredon
"""

def en_int(i):
    return "i" + str(i) + "e"


def en_bytes(b):
    return str(len(b)) + ":" + b.decode("utf-8")


def en_list(l):
    code = "l"
    for n in l:
        code = code + encode(n)
    return code + "e"


def en_dict(d):
    code = "d"
    for n in sorted(d.keys()):
        code = code + encode(n) + encode(d[n])
    return code + "e"


def encode(data):
    if type(data) == int:
        return en_int(data)
    elif type(data) == bytes:
        return en_bytes(data)
    elif type(data) == list:
        return en_list(data)
    elif type(data) == dict:
        return en_dict(data)


def de_int(i):
    x = 1
    while i[x] != "e":
        x = x + 1
    if len(i[x+1:]) == 0:
        return int(i[1: x])
    else:
        return [int(i[1: x]), i[x+1:]]


def de_bytes(b):
    x = 1
    while b[x] != ":":
        x = x + 1
    y = int(b[:x])
    if len(b[x + 1 + y:]) == 0:
        return b[x + 1:y+x+1].encode('utf-8')
    else:
        return [b[x + 1:y+x+1].encode('utf-8'), b[y+x+1:]]


def de_list(l):
    code = []
    data = l[1:]
    while data[0] != "e":
        x = decode(data)
        if type(x) == list:
            code.append(x[0])
            data = x[1]
        else:
            code.append(x)
            data = ""
            break
    if len(data) < 2:
        return code
    else:
        return [code, data[1:]]


def de_dict(d):
    code = {}
    data = d[1:]
    key = b''
    while data[0] != "e":
        x = decode(data)
        if type(x) == list:
            X = x[0]
            data = x[1]
        else:
            X = x
            data = ""
        if key == b'':
            key = X
        else:
            code[key] = X
            key = b''
        if data == "":
            break
    if len(data) < 2:
        return code
    else:
        return [code, data[1:]]


def decode(data):
    if data[0] == "i":
        return de_int(data)
    elif ord(data[0]) in range(48, 57):
        return de_bytes(data)
    elif data[0] == "l":
        return de_list(data)
    elif data[0] == "d":
        return de_dict(data)


z = {b'bar': b'spam', b'foo': [{b'ez': b'rty'}, 32]}
print(z)
print(encode(z))
print(decode(encode(z)))