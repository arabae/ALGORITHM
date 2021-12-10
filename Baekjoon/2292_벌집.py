"""
육각형으로 이루어진 벌집
중앙을 방 1로 두고, 이웃하는 방에 돌아가면서 1씩 증가하게 방번호를 부여
N이 주어졌을 때 1번에서 최소 개수의 방을 지나서 가면 이때 최소개수
"""

N = int(input())
start, idx = 1, 1
while start < N:
    start += 6*(idx)
    idx += 1
print(idx)