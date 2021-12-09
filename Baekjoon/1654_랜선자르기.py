"""
길이가 다른 K개의 랜선을 가지고 있으며,
N개의 같은 길이의 랜선으로 만들고 싶을때 최대 랜선의 길이
"""

K, N = map(int, input().split())

LANs = [int(input()) for _ in range(K)]
start, end = 1, max(LANs)

while start <= end:
    m = (end + start)//2
    split_lans = sum([l//m for l in LANs])

    if split_lans < N:
        end = m - 1
    else:
        start = m + 1

print(end)