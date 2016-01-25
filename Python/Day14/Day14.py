# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 18:54:55 2016

@author: Jake
"""

#Day14 - use modulo operations on the combination of their flytime and resttime.

input_string = open('input.txt', 'r')

content = input_string.readlines()
    
total_seconds = 2053
distances = dict()

for i in content:
    reindeer_name, _, _, speed, _, _, fly_time, _, _, _, _, _,_, rest_time, _ = i.split()    
    cycle_time = int(fly_time) + int(rest_time)
    distance_per_cycle = int(speed) * int(fly_time)
    number_of_cycles = int(total_seconds) / int(cycle_time)
    partial_cycle_seconds = int(total_seconds) % int(cycle_time) 
    
    cycle_distance = number_of_cycles * distance_per_cycle 
    partial_cycle_distance = distance_per_cycle if partial_cycle_seconds >= int(fly_time) else partial_cycle_seconds * int(speed)
    
    q, r = divmod(total_seconds, int(fly_time) + int(rest_time))
    distance = (q*int(fly_time) + min(r, int(fly_time))) * int(speed)
        
    distances[reindeer_name] = distance



for i in distances:

    q, r = divmod(total_seconds, travel + rest)
    distance = (q*travel + min(r, travel)) * speed
    
    

print [key for key,val in distances.iteritems() if val == max(distances.values())]


