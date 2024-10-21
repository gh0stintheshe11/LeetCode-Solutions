class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        from collections import Counter
        count = Counter(s)
        odd_count = sum(1 for v in count.values() if v % 2 != 0)
        return odd_count <= 1