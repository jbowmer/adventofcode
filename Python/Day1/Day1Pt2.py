# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:05:37 2015

@author: Jake
"""

#AdventofCode Day1 Part2

input_string = open('input.txt', 'r')

string = input_string.read()

count = 0
floor = 0
pos_counter = 0

for i in string:
    pos_counter = pos_counter + 1
    if i == '(':
        count = count + 1
    if i == ')':
        count = count - 1
    if count == - 1:
        print pos_counter
        exit

        