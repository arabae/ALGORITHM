A, B = map(int, input().split())
C, D = map(int, input().split())

nums = [A, B, C, D]
min_idx, max_value = 4, 0
for i in range(4):
    value = nums[0]/nums[2] + nums[1]/nums[3]
    nums = [nums[2], nums[0], nums[3], nums[1]]
    if max_value < value:
        min_idx, max_value = i, value

print(min_idx)