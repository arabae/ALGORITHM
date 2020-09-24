from collections import Counter

def solution(A):
    max_val = max(A)
    c = Counter(A)
    if len(c) == max_val == len(A): return 1
    else: return 0
