#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    bribe_num = 0
    Q = [i-1 for i in q]
    for idx, val in enumerate(Q):
        if val - idx > 2:
            print("Too chaotic")
            return 0
        for i in range(max(val-1, 0), idx):
            if Q[i] > val:
                bribe_num += 1
    print(bribe_num)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
