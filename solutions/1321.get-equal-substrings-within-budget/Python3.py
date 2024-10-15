class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        left = 0
        currentCost = 0
        maxLen = 0
        
        for right in range(n):
            currentCost += abs(ord(s[right]) - ord(t[right]))
            
            while currentCost > maxCost:
                currentCost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen