class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        count = Counter(s)
        
        for idx, char in enumerate(s):
            if count[char] == 1:
                return idx
        return -1