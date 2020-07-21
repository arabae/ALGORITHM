def sleeplessness(num):
    num_len = 0
    nums = [0] * 10
    k = 1
    while num_len != 10:
        k_num = k*num
        str_num = str(k_num)
        for j in range(len(str_num)):
            char_num = ord(str_num[j]) - 48
            nums[char_num] += 1

        k += 1
        num_len = 10 - nums.count(0)

    return num*(k-1)


T = int(input())
for i in range(1, T+1):
    N = int(input())
    answer = sleeplessness(N)
    print('#%d %d'%(i, answer))