N = int(input())
nums = list(map(int, input().split()))
cnt = 0

for n in nums:
    flag = True if n != 1 else False
    for i in range(2, n//2+1):
        if n%i == 0:
            flag = False
            break
    if flag:
        cnt += 1

print(cnt)