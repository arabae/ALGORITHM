# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    if A:
        K = K%len(A)
    answer = A[-K:]
    answer.extend(A[:-K])
    return answer


A = []
K = 0
print(solution(A, K))
