class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        def search(L):
            seen = set()
            for i in range(len(s) - L + 1):
                sub = s[i:i + L]
                if sub in seen:
                    return True
                seen.add(sub)
            return False
        
        left, right = 1, len(s)
        while left <= right:
            mid = (left + right) // 2
            if search(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return left - 1