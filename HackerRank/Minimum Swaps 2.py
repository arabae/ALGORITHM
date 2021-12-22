#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    Arr = [a-1 for a in arr]
    idx_dict = {v:i for i, v in enumerate(Arr)}
    swap_num = 0
    for idx, val in enumerate(Arr):
        if val != idx:
            cur_idx = idx_dict[idx]
            
            Arr[idx], Arr[cur_idx] = Arr[cur_idx], Arr[idx]
            idx_dict[val], idx_dict[idx] = cur_idx, idx
            
            swap_num += 1
    
    return swap_num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
