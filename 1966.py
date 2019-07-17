T = int(input())
for i in range(T):
    N = int(input())
    num = sorted(list(map(int, input().split())))
    print('#%d'%(i+1), end=' ')
    for j in num:
        print(j, end=' ')
    print()