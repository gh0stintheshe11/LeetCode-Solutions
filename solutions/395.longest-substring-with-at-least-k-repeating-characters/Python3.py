class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        def longest_substring_helper(s, k):
            if len(s) < k:
                return 0
            count = Counter(s)
            for char in count:
                if count[char] < k:
                    return max(longest_substring_helper(sub, k) for sub in s.split(char))
            return len(s)
        
        return longest_substring_helper(s, k)
        
from collections import Counter

# Create an instance of the Solution class
sol = Solution()

# Example test cases
print(sol.longestSubstring("aaabb", 3))  # Output: 3
print(sol.longestSubstring("ababbc", 2))  # Output: 5