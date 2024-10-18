class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        left, right = 0, len(nums) - 1
        result = 0
        
        # Precompute powers of 2 up to the length of nums
        power = [1] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            power[i] = (power[i - 1] * 2) % MOD
        
        while left <= right:
            if nums[left] + nums[right] <= target:
                result = (result + power[right - left]) % MOD
                left += 1
            else:
                right -= 1
        
        return result
