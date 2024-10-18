class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        i = 0
        
        while i < len(s):
            start = i
            while i < len(s) and s[i] == s[start]:
                i += 1
            if i - start >= 3:
                result.append([start, i - 1])
        
        return result