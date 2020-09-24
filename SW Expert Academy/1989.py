def palindrome(word):
    fr = 0
    ed = len(word) - 1
    while fr < ed:
        if word[fr] != word[ed]:
            return 0
        fr += 1
        ed -= 1
    return 1


T = int(input())
for i in range(1, T+1):
    s = input()
    print('#%d %d'%(i, palindrome(s)))