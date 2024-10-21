class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        prefix_xor = 0
        xor_count = {0: 1}
        beautiful_count = 0

        for num in nums:
            prefix_xor ^= num
            if prefix_xor in xor_count:
                beautiful_count += xor_count[prefix_xor]
            if prefix_xor in xor_count:
                xor_count[prefix_xor] += 1
            else:
                xor_count[prefix_xor] = 1

        return beautiful_count