def numlistmul(list1, n1, list2, n2):
    answer = []
    if n1 > n2:
        n1, n2 = n2, n1
        list1, list2 = list2, list1
    j = 0
    while j <= n2-n1:
        tmp = 0
        for k in range(n1):
            tmp += list1[k] * list2[j+k]
        answer.append(tmp)
        j += 1
    return max(answer)


T = int(input())
for i in range(1, T+1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print('#%d %d'%(i, numlistmul(A, n, B, m)))