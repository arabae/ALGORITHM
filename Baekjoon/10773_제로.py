k = int(input())
nums = []

for _ in range(k):
    n = int(input())
    if n != 0:
        nums.append(n)
    else:
        nums.pop()

print(sum(nums))