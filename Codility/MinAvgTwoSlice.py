def solution(A):
    min_idx, min_average, len_A = 0, 1000000, len(A)
    for P in range(len_A-1):
        val = A[P] + A[P+1]
        pr_average = val/2
        if min_average > pr_average:
            min_average = pr_average
            min_idx = P
        for Q in range(P+2, len_A):
            if pr_average > A[Q]:
                val += A[Q]
                pr_average = val/(Q-P+1)
                if Q == len_A-1:
                    if min_average > pr_average:
                        min_average = pr_average
                        min_idx = P
            else:
                if min_average > pr_average:
                    min_average = pr_average
                    min_idx = P
                break
    return min_idx

import random
# A = [random.randrange(-10, 10) for _ in range(30)]
A = [-7, -1, 4, 2, -4, 7, -3, -10, -3, -8, 4, -6, 9, -10, -7, -2, -8, 7, -7, 1, -4, 1, 7, 9, 3, -7, -4, 0, -9, 2]
print(A)
print(solution(A))