"""
알파벳 소문자로 이루어진 N개의 단어를 길이가 짧고, 같으면 사전순으로 정렬
주의, 같은 단어가 여러 번 입려되면 한 번씩 출력
"""

n_words = int(input())
words = set([input() for _ in range(n_words)]) # 중복 제거

alpha_sort = sorted(words) # 사전순으로 sort
len_sort = sorted(alpha_sort, key=lambda x:len(x)) # 길이순으로 sort

for word in len_sort:
    print(word)
