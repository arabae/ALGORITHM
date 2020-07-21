from collections import Counter

def solution(A):
    counter = Counter(A)
    print(counter)
    for k, v in counter.items():
        if v%2 == 1: return k


print(solution([7, 3, 1, 9, 9, 3, 1]))

