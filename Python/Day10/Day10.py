# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:54:32 2016

@author: Jake
"""

#AdventofCode, Day10

from itertools import groupby

def look_and_say(input):
    return ''.join(str(len(list(v))) + k for k, v in groupby(input))

p1 = input
for _ in range(40):
    p1 = look_and_say(p1)
print(len(p1))

p2 = input
for _ in range(50):
    p2 = look_and_say(p2)
print(len(p2))
