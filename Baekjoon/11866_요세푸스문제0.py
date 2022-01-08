import sys
input = sys.stdin.readline

n, k = map(int, input().split())
circle = list(range(1, n+1))
permut = []
idx = 0

while len(circle) != 0:
    idx = (idx + (k-1)) % len(circle)
    permut.append(str(circle.pop(idx)))

print(f"<{', '.join(permut)}>")
