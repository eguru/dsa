#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

max_sum = None
for i in range(len(arr) - 2):
    for j in range(len(arr) - 2):
        hour_glass = [ 
                        arr[i][j], arr[i][j+1], arr[i][j+2],    
                                   arr[i+1][j+1],
                        arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]
                     ]
        hour_glass_sum = reduce(lambda x, y: x+y, hour_glass)
        if max_sum < hour_glass_sum:
            max_sum = hour_glass_sum

print max_sum          
