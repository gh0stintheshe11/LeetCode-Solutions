class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        from collections import defaultdict
        
        n = len(s)
        if n < 3:
            return n
        
        left, right = 0, 0
        hashmap = defaultdict(int)
        max_len = 2
        
        while right < n:
            hashmap[s[right]] = right
            right += 1
            
            if len(hashmap) == 3:
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                left = del_idx + 1
            
            max_len = max(max_len, right - left)
        
        return max_len