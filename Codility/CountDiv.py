def solution(A, B, K):
    if A > K: start_val = A + A%K
    elif A == 0: start_val = A
    else: start_val = K

    end_val = B - B%K if B != 0 else B
    return (end_val-start_val)//K+1
