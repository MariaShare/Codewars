# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 17:53:52 2023

@author: Shadrina Maria
"""

'''Решение задачи _RGB to Hex_
Solution of task _RGB to Hex_
'''

def rgb(r, g, b):
    res = ""
    for i in (r, g, b):
        if i <= 0:
            res += "00"
        elif i >= 255:
            res += "FF"
        else:
            res += '%02x' % (i)
    res = res.upper()
    return res

print(rgb(167, 234, 197))