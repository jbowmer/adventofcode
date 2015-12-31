# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 18:43:22 2015

@author: Jake
"""

#Advent of Code, Day5

import re

input_string = open('input.txt', 'r')

with open('input.txt', 'r') as f:
    content = input_string.readlines()

nice_string_count = 0

def is_nice(s):
    vowels = 0
    for c in s:
        if c in 'aeiou':
            vowels += 1
        if vowels >= 3:
            break
    if vowels < 3:
        return False
    repeat = False
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            repeat = True
            break
    if not repeat:
        return False
    if 'ab' in s or 'cd' in s or 'pq' in s or 'xy' in s:
        return False
    return True    

for i in content:
    if is_nice(i):
        nice_string_count += 1
        
print nice_string_count

def is_really_nice(s):
    first = False
    for i in range(len(s) - 3):
        sub = s[i: i + 2]
        if sub in s[i + 2:]:
            first = True
            print("{} is really nice and repeats with {}".format(s, sub))
            break
    if not first:
        return False
    second = False
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            second = True
            break
    return second

really_nice_count = 0

for i in content:
    if is_really_nice(i):
        really_nice_count += 1

print really_nice_count


        
    
    