# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 21:18:08 2016

@author: Jake
"""

#AdventOfCode Day17

#Changemaking problem - but we bruteforce instead of recurse.

import itertools

input_string = open('input.txt', 'r')
content = input_string.readlines()

bottles = [int(i.split()[0]) for i in content]
total = 0

for i in range(len(bottles)):
    subtotal = 0
    for combination in itertools.combinations(bottles, i):
            if sum(combination) == 150:
                subtotal += 1
    total += subtotal
    print subtotal
    print total

