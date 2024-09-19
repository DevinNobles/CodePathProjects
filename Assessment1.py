import math
import os
import random
import re
import sys

#Write a function that returns the sum of all the Elements in a list. 

# Complete the 'find_sum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY lst as parameter.
#

def find_sum(lst):
    sum = 0
    # Write your code here
    for num in lst:
        sum += num
    return sum 



#!/bin/python3




#Write a function that finds the minimum value in a list of integers.

# Complete the 'find_min' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY lst as parameter.
#

def find_min(lst):
    # Write your code here
    min = lst[0]
    for num in lst:
        if num < min:
            min = num
    return min

"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    temp = input()
    
    if len(temp) > 60:
        input_string_new = temp
        chunks_new = input_string_new.split(", ")
        list_of_lists_new = [list(map(int, chunk.split())) for chunk in chunks_new]
        result = [find_min(lst) for lst in list_of_lists_new]
    else:
        result = find_min([int(n) for n in temp.split()])

    fptr.write(str(result) + '\n')

    fptr.close()


"""          
