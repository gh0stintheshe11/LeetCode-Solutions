class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        
        for i in range(n):
            # Odd length palindromes
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            # Even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        
        return count