class Solution:
    def makePalindrome(self, s: str) -> bool:
        mismatches = 0
        n = len(s)
        
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                mismatches += 1
        
        return mismatches <= 2