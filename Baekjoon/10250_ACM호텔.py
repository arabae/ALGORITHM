"""
정문에서 가장 짧은 거리에 있는 방을 선호함
H x W 호텔에서 층수는 관계없이, 엘레베이터에 내려서부터 걷는게 최소 (ex. 선호도: 102 < 302)
초기 모든 방은 비어있고, N번째로 도착한 손님에게 배정될 방 번호
"""

## H로 나누어 떨어지면 다음 방으로 가는 것

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    q, r = divmod(N, H)
    if r == 0:
        q, r = q-1, H
    print(f"{r}{q+1:02d}")
