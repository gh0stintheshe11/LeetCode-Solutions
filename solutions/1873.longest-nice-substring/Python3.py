class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        
        def is_nice(s: str) -> bool:
            char_set = set(s)
            for ch in char_set:
                if ch.swapcase() not in char_set:
                    return False
            return True
        
        max_len = 0
        result = ""
        
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if is_nice(s[i:j]) and j - i > max_len:
                    max_len = j - i
                    result = s[i:j]
        
        return result