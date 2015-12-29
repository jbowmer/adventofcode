# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 11:51:30 2015

@author: Jake
"""

#AdventofCode Day1 Python

input_string = open('input.txt', 'r')

string = input_string.read()

count = 0
floor = 0

for i in string:
    if i == '(':
        count = count + 1
    if i == ')':
        count = count - 1
        

result = floor + count
