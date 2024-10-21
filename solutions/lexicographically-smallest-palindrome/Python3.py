class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        n = len(s)
        
        for i in range(n // 2):
            if s[i] != s[n - i - 1]:
                smallest_char = min(s[i], s[n - i - 1])
                s[i] = smallest_char
                s[n - i - 1] = smallest_char
                
        return ''.join(s)