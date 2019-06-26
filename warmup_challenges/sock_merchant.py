#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    num_pairs = 0
    
    sock_color_count = defaultdict(int) 
    for sock_color in ar:
      sock_color_count[sock_color] += 1
    
    for sock_color in sock_color_count.keys():
      num_pairs += sock_color_count[sock_color] // 2

    return num_pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

