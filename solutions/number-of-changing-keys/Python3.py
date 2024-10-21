class Solution:
    def countKeyChanges(self, s: str) -> int:
        lower_s = s.lower()
        count = 0
        for i in range(1, len(lower_s)):
            if lower_s[i] != lower_s[i - 1]:
                count += 1
        return count