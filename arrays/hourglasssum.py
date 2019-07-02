#!/bin/python3

import math
import os
import random
import re
import sys

def calculateHourGlassSum(arr, i, j):
  s = 0
  for m in range(i, i+3):
    for n in range(j, j+3):
      if m == i + 1 and n != j + 1:
        continue
      s += arr[m][n]
  
  return s 

# Complete the hourglassSum function below.
def hourglassSum(arr):
  s = float('-inf')
  for i in range(4):
    for j in range(4):
      s = max(s, calculateHourGlassSum(arr, i, j))
  
  return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

