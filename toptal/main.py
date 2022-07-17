# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#Downloaded 

import math

def solution(X, B, Z):
    # write your code in Python 3.6
    if len(B) < Z :
        Z = len(B)
    
    arr_sum = sum(B)
    observation_sum = sum(B[len(B)-Z:])    
    remaining_time = X - arr_sum

    if Z < 1:
        return -1
    else:
        return math.ceil(remaining_time / (observation_sum/Z))

print( solution( 100, [10,6,6,8], 5 ) )image.png