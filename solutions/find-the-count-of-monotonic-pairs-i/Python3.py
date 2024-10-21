class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        cap = max(nums)
        n = len(nums)
        count = [0] * (cap+1)
        
        for j in range(0, nums[0]+1):
            count[j] = 1

        for i in range(1, n):
            prefix_sum = list(accumulate(count))
            count = [0] * (cap+1)
            for j in range(nums[i]+1):
                upper_bound = min(nums[i-1]-nums[i]+j,j)
                if upper_bound >= 0:
                    count[j] = prefix_sum[upper_bound] % MOD
        return sum(count) % MOD