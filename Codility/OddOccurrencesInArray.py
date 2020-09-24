from collections import Counter

def solution(A):
    counter = Counter(A)
    print(counter)
    for k, v in counter.items():
        if v%2 == 1: return k
