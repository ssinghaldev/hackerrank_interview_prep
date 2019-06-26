#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
  num_valleys = 0
  pos = 0
  
  for path in s:
    if path == 'U':
      pos += 1
    elif path == 'D':
      pos -= 1
      if pos == -1:
        num_valleys += 1
  
  return num_valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

