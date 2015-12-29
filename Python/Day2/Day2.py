# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:12:32 2015

@author: Jake
"""

#AdventofCode Day2

input_string = open('input.txt', 'r')

with open('input.txt', 'r') as f:
    content = input_string.readlines()

wrapping_paper = 0
    
for i in content:
    width, height, length = i.replace('\n', '').split('x')
    width = int(width)
    height = int(height)
    length = int(length)    
    dimensions = [width * height, height * length, length * width]
    paper_required = 2 * dimensions[0] + 2 * dimensions[1] + 2 * dimensions[2] + min(dimensions)
    
    wrapping_paper = wrapping_paper + paper_required
    
print wrapping_paper