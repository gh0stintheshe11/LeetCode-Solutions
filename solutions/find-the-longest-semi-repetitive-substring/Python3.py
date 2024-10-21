class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 1
        left = 0
        adjacent_pair_count = 0
        
        for right in range(1, n):
            if s[right] == s[right - 1]:
                adjacent_pair_count += 1
            
            while adjacent_pair_count > 1:
                if s[left] == s[left + 1]:
                    adjacent_pair_count -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length