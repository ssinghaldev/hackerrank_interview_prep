#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    len_s = len(s)
    
    num_times_full = n // len_s
    partial_string_len = n % len_s

    num_a = 0
    num_a_partial = 0
    
    l = 0
    for char in s:
        if char == 'a':
            num_a += 1
        
        l += 1
        if l == partial_string_len:
            num_a_partial = num_a
    
    return (num_a*num_times_full) + num_a_partial

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

