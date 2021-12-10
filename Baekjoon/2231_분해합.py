"""
어떤 자연수 N이 있을 때, N의 분해합은 N과 N을 이루는 각 자리수의 합
M의 분해합이 N: M을 N의 생성자라함
ex. 245 => 245+ 2+ 4+ 5 = 256 (245는 256의 생성자)
N이 주어졌을 때, N의 가장 작은 생성자 구하기 (없으면 0)
"""

N = int(input())
answer = 0
for i in range(1, N+1):
    if i + sum(map(int, list(str(i)))) == N:
        answer = i
        break
print(answer)
