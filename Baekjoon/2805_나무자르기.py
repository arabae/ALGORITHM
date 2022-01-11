import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
l, r = 0, max(trees)

while l <= r:
    mid = (l+r)//2
    split_tree = 0
    for t in trees:
        if t > mid:
            split_tree += (t - mid)
        if split_tree >= m:
            break
            
    if split_tree >= m:
        l = mid + 1
    else:
        r = mid - 1

print(r)