class Solution:
    def balancedString(self, s: str) -> int:
        from collections import Counter
        
        n = len(s)
        target = n // 4
        count = Counter(s)

        # Check if already balanced
        if all(count[char] == target for char in "QWER"):
            return 0
        
        # Two pointers
        left = 0
        min_len = n
        for right in range(n):
            count[s[right]] -= 1
            
            while all(count[char] <= target for char in "QWER"):
                min_len = min(min_len, right - left + 1)
                count[s[left]] += 1
                left += 1
                
        return min_len