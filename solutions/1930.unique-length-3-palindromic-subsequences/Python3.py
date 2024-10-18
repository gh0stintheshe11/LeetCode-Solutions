class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0
        for char_code in range(26):
            char = chr(char_code + ord('a'))
            first, last = -1, -1
            
            # Find the first and last occurrence of the char in s
            for i in range(len(s)):
                if s[i] == char:
                    if first == -1:
                        first = i
                    last = i
            
            if first != -1 and last != -1 and last - first >= 2:
                # We need to find unique characters between first and last occurrence of char
                unique_chars = set(s[first + 1:last])
                result += len(unique_chars)
        
        return result