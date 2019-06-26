#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
  num_steps = 0
  c_idx  = 0
  while c_idx < len(c) - 1:
    if c_idx + 2 < len(c) and c[c_idx + 2] != 1:
      c_idx += 2
    else:
      c_idx += 1
      
    num_steps += 1
  
  return num_steps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

