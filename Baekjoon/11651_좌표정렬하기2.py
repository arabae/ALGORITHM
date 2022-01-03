import sys

N = int(sys.stdin.readline())

locations = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
locations.sort(key=lambda x: (x[1], x[0]))

for x, y in locations:
    print(x, y)