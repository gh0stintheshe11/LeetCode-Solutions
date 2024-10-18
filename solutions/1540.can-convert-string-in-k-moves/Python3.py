class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        shift_counts = [0] * 26

        for i in range(len(s)):
            shift = (ord(t[i]) - ord(s[i])) % 26
            if shift > 0:
                shift_counts[shift] += 1

        for shift in range(1, 26):
            max_shifts_needed = shift + (shift_counts[shift] - 1) * 26
            if max_shifts_needed > k:
                return False

        return True