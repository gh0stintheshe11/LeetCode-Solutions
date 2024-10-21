class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        max_length = 0
        count_zero = 0
        count_one = 0
        
        i = 0
        while i < len(s):
            count_zero = count_one = 0
            
            while i < len(s) and s[i] == '0':
                count_zero += 1
                i += 1
            
            while i < len(s) and s[i] == '1':
                count_one += 1
                i += 1
            
            max_length = max(max_length, 2 * min(count_zero, count_one))
        
        return max_length