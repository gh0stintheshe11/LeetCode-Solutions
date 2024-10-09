class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            current_char = s[left]
            while left <= right and s[left] == current_char:
                left += 1
            while left <= right and s[right] == current_char:
                right -= 1
        return right - left + 1