class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        L = len(bin(max(nums))) - 2
        max_xor = 0
        for i in range(L)[::-1]:
            max_xor <<= 1
            curr_xor = max_xor | 1
            prefixes = {num >> i for num in nums}
            if any(curr_xor ^ p in prefixes for p in prefixes):
                max_xor = curr_xor
        return max_xor