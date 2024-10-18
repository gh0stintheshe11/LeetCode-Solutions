class Solution:
    def minOperations(self, n: int) -> int:
        operations = 0
        while n > 0:
            # Find the rightmost bit that is set
            lowest_set_bit = n & -n
            # Check if the next adjacent bit is also set
            if (n & (lowest_set_bit << 1)):
                # If it's set, add the current lowest_set_bit to move carry over
                n += lowest_set_bit
            else:
                # Otherwise, subtract it
                n -= lowest_set_bit
            # This counts as one operation
            operations += 1
        return operations