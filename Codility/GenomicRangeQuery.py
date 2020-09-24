def solution(S, P, Q):
    M = []
    for i in range(len(P)):
        idx = S[P[i]:Q[i]+1].find('A')
        if idx != -1:
            M.append(1)
        else:
            idx = S[P[i]:Q[i]+1].find('C')
            if idx != -1:
                M.append(2)
            else:
                idx = S[P[i]:Q[i]+1].find('G')
                if idx != -1:
                    M.append(3)
                else:
                    M.append(4)
    return M

solution('A', [0], [0])