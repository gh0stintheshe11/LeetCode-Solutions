class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        max_len = [0] * 26
        curr_len = 0

        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i - 1]) in (1, -25)):
                curr_len += 1
            else:
                curr_len = 1
            
            index = ord(s[i]) - ord('a')
            max_len[index] = max(max_len[index], curr_len)

        return sum(max_len)