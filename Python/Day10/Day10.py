# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:54:32 2016

@author: Jake
"""

#AdventofCode, Day10

input_string = '1321131112'

new_string = ''
n = 1
while n < 41:
    new_string = ''    
    count = 1
    for i in range(len(input_string)):
        int_name = input_string[i]
        try:
            if input_string[i + 1] == input_string[i]:
                count += 1         
            else:
                new_string = new_string + str(count) + int_name
                count = 1
        except:
            if input_string[i -1] == input_string[i]:
                new_string = new_string + str(count) + int_name
            else:
                new_string = new_string + str(count) + int_name 
        #print new_string
    input_string = new_string
    n += 1
    
print len(new_string)