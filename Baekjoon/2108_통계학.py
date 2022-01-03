import sys
N = int(sys.stdin.readline())

nums = [int(sys.stdin.readline()) for _ in range(N)]
nums.sort()
mode_cnt, cnt = 0, [0] * 8001
for i in nums:
    cnt[i+4000] += 1

flag = True
for idx, val in enumerate(cnt):
    if val == 0: continue
    if val > mode_cnt:
        mode = idx-4000
        mode_cnt = val
        flag = True
    elif val == mode_cnt and flag:
        if mode < idx-4000:
            mode = idx-4000
            flag = False

print(round(sum(nums)/N))
print(nums[N//2])
print(mode)
print(nums[-1] - nums[0])
