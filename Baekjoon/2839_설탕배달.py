"""
설탕을 정확하게 N킬로그램을 배달 -- 봉지는 3, 5킬로그램이 있음
최대한 적은 봉지를 들고가려할 때, 봉지를 몇 개 가져가면 되는지?
"""

N = int(input())
bags = 0
while N > 0:
    if N % 5 == 0:
        bags += N//5
        break
    bags += 1
    N -= 3
if N < 0: bags = -1
print(bags)