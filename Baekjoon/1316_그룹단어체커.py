def group_word_checker(w):
    unique_set = []
    if len(w) <= 1:
        return True

    for i in range(len(w)-1):
        if w[i] in unique_set:
            return False

        if w[i] != w[i+1]:
            unique_set.append(w[i])

    if w[-1] not in unique_set:
        return True
    else:
        return False

N = int(input())
cnt = 0
for _ in range(N):
    word = input()
    if group_word_checker(word):
        cnt += 1
print(cnt)
