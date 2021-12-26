"""
k명의 사람이 n개의 꽃을 모두 사는 최소 금액
- c: 꽃들의 가격
    - 이전에 한번 구매하면 가격이 배로 올라감 
    (current purchases + previous purchases) * price
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    n = len(c)
    if n <= k: 
        return sum(c)
    
    c = sorted(c, reverse=True)
    
    total_price, purchase = 0, 0
    for i, price in enumerate(c):
        total_price += (purchase + 1) * price
        if (i+1)%k == 0:
            purchase += 1
    return total_price

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
