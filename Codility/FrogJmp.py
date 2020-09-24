def solution(X, Y, D):
    q, r = divmod(Y-X, D)
    if r != 0:
        q += 1
    return q
