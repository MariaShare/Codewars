# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 09:11:14 2023

@author: Shadrina Maria
"""

'''Решение задачи _Convert string to camel case_
Solution of task _Convert string to camel case_
'''

def to_camel_case(text):
    text = list(text)
    for i in range(len(text)):
        if text[i] in '-_':
            text[i] = ' '
    text = ''.join(text).split()
    t = ""
    for i in range(0, len(text)):
        t += text[i].title()
    return t

print(to_camel_case("the-stealth_warrior"))
print(to_camel_case("the_stealth_warrior"))