""""
중복되지 않은 단어의 개수와
input 단어 순서대로(중복 단어는 한 번만) 몇 번 나왔는지 출력
"""
from collections import Counter

n = int(input())
words = [input() for _ in range(n)]

word_cnt = Counter(words)
print(len(word_cnt))
for cnt in word_cnt.values():
    print(cnt, end=' ')