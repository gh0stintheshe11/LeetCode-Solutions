class Solution:
    def maxNumber(self, n: int) -> int:
        # Find the most significant bit position that is set in n
        msb_position = n.bit_length()
        return (1 << (msb_position - 1)) - 1