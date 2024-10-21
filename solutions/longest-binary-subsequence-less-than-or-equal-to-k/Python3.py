class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        count_zeros = s.count('0')
        current_value = 0
        num_bits = 0

        # Add 1s from the right
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                if num_bits < 30 and current_value + (1 << num_bits) <= k:
                    current_value += (1 << num_bits)
                    num_bits += 1
            else:
                num_bits += 1

        return count_zeros + min(num_bits, n) - count_zeros