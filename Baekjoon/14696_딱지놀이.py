# 별(4) > 동그라미(3) > 네모(2) > 세모(1)
import sys
from collections import defaultdict
input = sys.stdin.readline

def winner(ddakji_a, ddakji_b):
    for i in range(4, 0, -1):
        if ddakji_a[i] > ddakji_b[i]:
            return 'A'
        elif ddakji_a[i] < ddakji_b[i]:
            return 'B'
    return 'D'
        
N = int(input())
for _ in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    info_a = defaultdict(int)
    info_b = defaultdict(int)

    for a in A[1:]:
        info_a[a] += 1
    for b in B[1:]:
        info_b[b] += 1

    print(winner(info_a, info_b))
