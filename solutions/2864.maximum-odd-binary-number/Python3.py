class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_count = s.count('1')
        zero_count = len(s) - one_count
        # Ensure one '1' at the end to make it odd, rest `one_count - 1` ones at the start
        return '1' * (one_count - 1) + '0' * zero_count + '1'