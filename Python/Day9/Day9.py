# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 12:34:03 2016

@author: Jake
"""

#Advent of Code - Day9

from itertools import permutations
from collections import defaultdict

input_string = open('input.txt', 'r')

with open('input.txt', 'r') as f:
    content = input_string.readlines()

places = set()
graph = defaultdict(dict)

for i in content:
    source, _, dest, _, distance = i.split()
    places.add(source)
    places.add(dest)
    graph[source][dest] = int(distance)
    graph[dest][source] = int(distance)
    
distances = []

for i in permutations(places):
    distances.append(sum(map(lambda x, y: graph[x][y], i[:-1], i[1:])))
    
print min(distances)
print max(distances)
