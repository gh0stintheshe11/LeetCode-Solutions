class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        
        from collections import Counter
        char_count = Counter(s)
        
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
        
        return odd_count <= k