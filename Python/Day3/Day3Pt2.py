# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 18:31:16 2015

@author: Jake
"""

#AdventofCode Day3 Part 2

#We modify the original - tracking both regular santa and robot_santa
input_string = open('input.txt', 'r')

string = input_string.read()

santa_string = string[::2]
robot_string = string[1::2]

start_location = [0,0]

x_loc = 0
y_loc = 0

visited_locations_santa = []
visited_locations_santa.append(start_location)

for i in santa_string:
    if i == '^':
        y_loc = y_loc + 1
    if i == 'v':
        y_loc = y_loc - 1
    if i == '>':
        x_loc = x_loc + 1
    if i == '<':
        x_loc = x_loc - 1
    
    new_loc = [x_loc, y_loc]
    visited_locations_santa.append(new_loc)
    
#now for the robot
start_location = [0,0]

x_loc = 0
y_loc = 0

visited_locations_robot = []
visited_locations_robot.append(start_location)

for i in robot_string:
    if i == '^':
        y_loc = y_loc + 1
    if i == 'v':
        y_loc = y_loc - 1
    if i == '>':
        x_loc = x_loc + 1
    if i == '<':
        x_loc = x_loc - 1
    
    new_loc = [x_loc, y_loc]
    visited_locations_robot.append(new_loc)
    
total_visited = visited_locations_santa + visited_locations_robot

seen = list()
for i in total_visited:
    if i not in seen:
        seen.append(i)
        
print len(seen)