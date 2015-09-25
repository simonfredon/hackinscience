# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 12:12:00 2015

@author: simonfredon
"""

def int_encode(integ):
    return 'i' + str(integ) + 'e'


def bytes_encode(byte):
    return str(len(byte)) + ':' + (str(byte))[2:-1]


def list_encode(lists):
    for i in range(len(lists)):
        lists[i] = encode2(lists[i])
    return 'l' + ''.join([str(i) for i in lists]) + 'e'


def dict_encode(dicts):
    clean = []
    for i in dicts:
        dicts[i] = encode2(dicts[i])
        dicts[encode2(i)] = dicts.pop(i)
    for key, value in sorted(dicts.items(),
                             key=lambda st: st[0].split(':')[1]):
        clean.append(str(key))
        clean.append(str(value))
    print(sorted(dicts.items()))
    print(clean)
    return 'd' + ''.join([i for i in clean]) + 'e'


def str_encode(stri):
    return stri


bencode_dic = {"<class 'int'>": int_encode, "<class 'bytes'>": bytes_encode,
               "<class 'list'>": list_encode, "<class 'dict'>": dict_encode,
               "<class 'str'>": str_encode}


def encode2(obj):
    if type(obj) == bytes or int:
        return bencode_dic[str(type(obj))](obj)
    elif type(obj) == dict:
        for i in obj:
            obj[i] = bencode_dic[str(type(obj[i]))](obj)[i]
        return obj
    elif type(obj) == list:
        for i in range(len(list)):
            obj[i] = bencode_dic[str(type(obj[i]))](obj)[i]
        return obj
    else:
        return obj