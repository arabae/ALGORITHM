class Solution:
    def countSubstrings(self, s: str) -> int:
        n_palindromic = len(s)
        for j in range(2, len(s)+1):
            for i in range(len(s)-j+1):
                if s[i:i+j] == s[i:i+j][::-1]: n_palindromic += 1
                
        return n_palindromic
