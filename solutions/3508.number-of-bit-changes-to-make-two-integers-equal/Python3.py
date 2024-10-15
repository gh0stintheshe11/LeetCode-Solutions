class Solution:
    def minChanges(self, n: int, k: int) -> int:
        # XOR will give the bits that are different
        xor_result = n ^ k
        # Count the number of 1-bits, which are the changes needed
        changes = bin(xor_result).count('1')
        return changes if (n | k) == n else -1