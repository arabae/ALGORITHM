def merge_the_tools(string, k):
    for idx in range(0, len(string), k):
        new_word = ""
        for sub in string[idx:idx+k]:
            if sub not in new_word:
                new_word += sub
        print(new_word)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)