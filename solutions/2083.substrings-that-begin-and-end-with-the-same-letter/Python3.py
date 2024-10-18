class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        from collections import defaultdict

        count = defaultdict(int)
        total_substrings = 0

        for char in s:
            count[char] += 1

        for char in count:
            n = count[char]
            total_substrings += n * (n + 1) // 2

        return total_substrings