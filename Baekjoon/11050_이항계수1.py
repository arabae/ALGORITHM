"""
자연수 N과 정수 K가 주어졌을 때 이항 계수 (N, K)를 구하라
- 이항 계수: (5, 2) -- 5!/2!3! -- 10
- k< 0 or k > n -- 0 => input 조건에서 걸러짐
"""

N, K = map(int, input().split())
n, k = 1, 1
for i in range(N, N-K, -1):
    n *= i
for i in range(K, 0, -1):
    k *= i
print(n//k)