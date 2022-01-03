import sys
N = int(sys.stdin.readline())
nums = [0] * 10001
for _ in range(N):
    nums[int(sys.stdin.readline())] += 1

for i, v in enumerate(nums):
    if v != 0:
        for _ in range(v):
            print(i)
