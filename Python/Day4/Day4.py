# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:00:08 2016

@author: Jake
"""

#AdventOfCode, day4.

input_string = 'bgvyzdsv'

from hashlib import md5

for i in range(1000):
    hash = md5((input_string + str(i)).encode()).hexdigest()
    if h[:5] == '00000':
        print(h)
        break