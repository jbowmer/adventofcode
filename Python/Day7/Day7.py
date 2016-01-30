# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:15:21 2016

@author: Jake
"""

#AdventOfCode Day7

input_string = open('input.txt', 'r')

content = input_string.readlines()

wires = {}

for i in content:
    instructions, wire = i.split('->')

    print instructions, wire    
