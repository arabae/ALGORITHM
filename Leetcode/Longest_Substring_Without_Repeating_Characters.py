class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_len = 0

        for i in range(len(s)):
            sub_string = s[i]
            for j in range(i+1, len(s)):

                if s[j] not in sub_string:
                    sub_string += s[j]
                else:
                    break
                
            longest_len = max(longest_len, len(sub_string))
        return longest_len
