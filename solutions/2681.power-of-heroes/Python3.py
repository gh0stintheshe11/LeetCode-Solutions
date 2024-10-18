class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        result = 0
        prefix_sum = 0
        
        for num in nums:
            result = (result + num * num % MOD * (prefix_sum + num) % MOD) % MOD
            prefix_sum = (prefix_sum * 2 + num) % MOD
        
        return result