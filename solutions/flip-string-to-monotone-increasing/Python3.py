class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        ones_count = 0
        flips = 0
        
        for i in range(n):
            if s[i] == '0':
                flips = min(flips + 1, ones_count)
            else:
                ones_count += 1
        
        return flips