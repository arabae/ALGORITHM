"""
거주조건: a층 b호에 살려면 (a-1)층의 1호~b호까지 사람들의 수의 합만큼 데려와 살아야함
k층 n호에 몇 명이 살고 있는지 (0층 1호부터 -- 0층 i호는 i명만 삶)
"""

T = int(input())
for _ in range(T):
    k = int(input()) + 1
    n = int(input())

    people = [[0 for _ in range(n)] for _ in range(k)]
    for i in range(n):
        people[0][i] = i + 1
    for i in range(k):
        people[i][0] = 1
    
    for i in range(1, k):
        for j in range(1, n):
            people[i][j] = people[i-1][j] + people[i][j-1]
    
    print(people[k-1][n-1])