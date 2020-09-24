from collections import Counter

def solution1(N, A):
    change_max_all, sub_change = [i for i, v in enumerate(A) if v == N+1], []
    if change_max_all:
        if change_max_all[0] != 0:
            sub_change.append(change_max_all[0])
    for i in range(1, len(change_max_all)):
        if change_max_all[i-1]+1 == change_max_all[i]:
            continue
        sub_change.append(change_max_all[i])
    s, max_value = 0, 0
    for i in sub_change:
        most_value = Counter(A[s:i]).most_common(2)
        if most_value[0][0] != N+1: max_value += most_value[0][1]
        elif len(most_value) == 2: max_value += most_value[1][1]
        s = i+1

    s, counter = -1, [max_value]*N
    if sub_change:
        s = sub_change[-1]
    for i in range(s+1, len(A)):
        if A[i] != N+1:
            counter[A[i]-1] += 1

    return counter

def solution2(N, A):
    lastmax, max_val = 0, 0
    counter = [0]*N
    for i in range(len(A)):
        if A[i] < N+1:
            j = A[i] - 1
            if counter[j] < lastmax: counter[j] = lastmax
            counter[j] += 1
            if max_val < counter[j]: max_val = counter[j]
        else: lastmax = max_val

    for i in range(N):
        if counter[i] < lastmax: counter[i] = lastmax
    return counter