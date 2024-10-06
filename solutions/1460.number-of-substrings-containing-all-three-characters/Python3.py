class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = [0, 0, 0]
        result = 0
        left = 0
        
        for right in range(len(s)):
            count[ord(s[right]) - ord('a')] += 1
            
            while all(count):
                count[ord(s[left]) - ord('a')] -= 1
                left += 1
            
            result += left
        
        return result