class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palin_str = ""
        max_len = 0
        
        for i in range(len(s)):
            if s[i-(max_len+1)+1:i+1] == s[i-(max_len+1)+1:i+1][::-1]:
                longest_palin_str = s[i-(max_len+1)+1:i+1]
                max_len += 1
                
            elif i-(max_len+2)+1 >= 0 and s[i-(max_len+2)+1:i+1] == s[i-(max_len+2)+1:i+1][::-1]:
                longest_palin_str = s[i-(max_len+2)+1:i+1]
                max_len += 2

        return longest_palin_str
        