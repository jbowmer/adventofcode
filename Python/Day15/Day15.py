# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 17:34:52 2016

@author: Jake
"""

#AdventofCode, Day15

input_string = open('input.txt', 'r')

content = input_string.readlines()

ingredients = {}
    
best_total = 0


for i in content:
    ingredient, _, capacity, _, durability, _, flavour, _, texture, _, calories = i.split()
    
    ingredients[ingredient] = [capacity, durability, flavour, texture, calories]
    
print ingredients






def get_total(F, C, B, S):
    cap = max(4 * F - B, 0)
    dur = max(-2 * F + 5 * C, 0)
    fla = max(-C + 5 * B - 2 * S, 0)
    tex = max(2 * S, 0)
    cal = max(5 * F + 8 * C + 6 * B + S, 0)
    return cap * dur * fla * tex, cal

best_total = 0
for F in range(0, 101):
    for C in range(0, 100 - F + 1):
        for B in range(0, 100 - (F + C) + 1):
            S = 100 - (F + C + B)
            total, cal = get_total(F, C, B, S)
            if total > best_total and cal == 500:
                best_total = total
print best_total