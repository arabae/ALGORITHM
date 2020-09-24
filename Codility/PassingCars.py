def solution(A):
    cnt, answer = 0, 0
    n_one = A.count(1)
    for i in A:
        if i == 1:
            cnt += 1
        else:
            answer += (n_one - cnt)
            cnt = 0
    if answer > 1000000000:
        return -1

    return answer