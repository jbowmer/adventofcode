# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 20:13:02 2016

@author: Jake
"""

#Advent of code, day12
import sys
import re

input_string = open('input.txt', 'r')
string = input_string.read()
input_string.close()

print "Sum of all numbers 1:", sum(map(int, re.findall("-?[0-9]+", string)))