#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    prefix_sum = [0 for _ in range(n)]
    for a, b, k in queries:
        prefix_sum[a-1] += k
        if b < n:
            prefix_sum[b] -= k
    
    max_val, summand = 0, 0
    for val in prefix_sum:
        summand += val
        if summand > max_val: max_val = summand
    
    return max_val
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
