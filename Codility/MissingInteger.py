def solution(A):
    A = sorted(set([x for x in A if x > 0]))
    A.insert(0, 0)
    for i, v in enumerate(A):
        if i != v: return i
    return len(A)
