# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 12:24:01 2015

@author: Jake
"""

#Day8 ADventofCode

import re

input_string = open('input.txt', 'r')

with open('input.txt', 'r') as f:
    content = input_string.readlines()

def raw_char_count(s):
    return len(s)

def escaped_char_count(s):
    count = 0
    i = 1
    while i < len(s) - 1:
        if s[i] == "\\":
            i += 4 if s[i+1] == "x" else 2
        else:
            i += 1
        count += 1
    return count
    
raw = 0
escaped = 0    

for i in content:
    raw += raw_char_count(i)
    escaped += escaped_char_count(i)

print raw-escaped