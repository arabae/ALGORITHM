"""
string S가 있을 때, character 'c'가 string에서 X번 발생 -> (X, c)로 표기
"""

S = input()

char, char_cnt = S[0], 1
consecutive_occurence = []

for s in S[1:]:
    if char != s:
        consecutive_occurence.append((char_cnt, int(char)))
        char, char_cnt = s, 0
    char_cnt += 1

consecutive_occurence.append((char_cnt, int(char)))
for co in consecutive_occurence:
    print(co, end=' ')
