"""
팰린드롬: 뒤에서부터 읽어도 똑같은 단어 -- 한글자도 팰린드롬
팰린드롬이면 yes, 아니면 no 출력
"""

def is_palindrome(w):
    for i in range(len(word)//2):
        if word[i] != word[len(word)-i-1]:
            return 'no'
    return 'yes'

while True:
    word = input()
    if "0" == word: break

    result = is_palindrome(word)
    print(result)
