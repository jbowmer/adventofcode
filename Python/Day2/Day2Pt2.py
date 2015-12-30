# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:58:59 2015

@author: Jake
"""

#AdventofCode Day2Pt2

input_string = open('input.txt', 'r')

with open('input.txt', 'r') as f:
    content = input_string.readlines()
    
ribbon = 0

for i in content:
    width, height, length = i.replace('\n', '').split('x')
    width = int(width)
    height = int(height)
    length = int(length)
    
    perimeters = [2 * (width + height), 2 * (height + length), 2 * (length+width)]
    
    wrap_ribbon = min(perimeters)
    bow_ribbon = width * height * length
    ribbon = ribbon + wrap_ribbon + bow_ribbon
    

print ribbon
    
    