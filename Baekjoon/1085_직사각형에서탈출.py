"""
왼쪽 아래 꼭짓점은 (0, 0) 오른쪽 위 꼭지점은 (w, h)인 직사각형 존재
한수가 (x, y)에 있을때 직사각형의 경계선까지 가는 거리의 최솟값
"""

x, y, w, h = map(int, input().split())

min_distance = min(abs(x - w), abs(y - h), abs(x - 0), abs(y - 0))
print(min_distance)