# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:00:08 2016

@author: Jake
"""

#AdventOfCode, day4.

input_string = 'bgvyzdsv'

from hashlib import md5

#Part I
for i in range(1000000):
    hash_string = md5((input_string + str(i)).encode()).hexdigest()
    if hash_string[:5] == '00000':
        print hash_string
        print i
        break
    

#Part II

for i in range(10000000):
    hash_string = md5((input_string + str(i)).encode()).hexdigest()
    if hash_string[:6] == '000000':
        print hash_string
        print i
        break