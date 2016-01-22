# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:12:45 2016

@author: Jake
"""

#AdventOfCode, Day13.

from itertools import permutations
from collections import defaultdict

input_string = open('input.txt', 'r')


relations = defaultdict(dict)

with open('input.txt', 'r') as f:
    content = input_string.readlines()
    

for i in content:
    line = i[:-2].split()    
    
    person_one = line[0]
    person_two = line[10]

    #print person_one, person_two
    happiness = line[3]
    #print person_one, person_two, happiness    
    
    relations[person_one][person_two] = int(happiness) if line[2] == 'gain' else -int(happiness)


seatings = list(permutations(relations.keys()))
max_happiness = 0
for seating in seatings:
    happiness = 0
    for i in range(0, len(seating)):
        try:
            happiness += relations[seating[i]][seating[i+1]]
        except IndexError:
            happiness += relations[seating[i]][seating[0]]
        try:
            happiness += relations[seating[i]][seating[i-1]]
        except IndexError:
            happiness += relations[seating[i]][seating[-1]]
    if happiness > max_happiness:
        max_happiness = happiness

print(max_happiness)

#Part2


for k in list(relations.keys()):
    relations['me'][k] = 0
    relations[k]['me'] = 0

seatings = list(permutations(relations.keys()))
max_happiness = 0
for seating in seatings:
    happiness = 0
    for i in range(0, len(seating)):
        try:
            happiness += relations[seating[i]][seating[i+1]]
        except IndexError:
            happiness += relations[seating[i]][seating[0]]
        try:
            happiness += relations[seating[i]][seating[i-1]]
        except IndexError:
            happiness += relations[seating[i]][seating[-1]]
    if happiness > max_happiness:
        max_happiness = happiness

print(max_happiness)


