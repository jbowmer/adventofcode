# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 18:15:18 2015

@author: Jake
"""

#Advent of code, day3

input_string = open('input.txt', 'r')

string = input_string.read()


start_location = [0,0]

x_loc = 0
y_loc = 0

visited_locations = []
visited_locations.append(start_location)

for i in string:
    if i == '^':
        y_loc = y_loc + 1
    if i == 'v':
        y_loc = y_loc - 1
    if i == '>':
        x_loc = x_loc + 1
    if i == '<':
        x_loc = x_loc - 1
    
    new_loc = [x_loc, y_loc]
    visited_locations.append(new_loc)

#get unique values

seen = list()
for i in visited_locations:
    if i not in seen:
        seen.append(i)

#number of hosues visited at least once:
print len(seen)