class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        xor_sum = 0
        while n:
            xor_sum ^= n
            n >>= 1
        return xor_sum