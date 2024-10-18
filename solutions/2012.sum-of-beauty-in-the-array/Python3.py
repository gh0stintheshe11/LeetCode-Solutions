class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Calculate prefix maximums
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], nums[i])
        
        # Calculate suffix minimums
        suffix = [0] * n
        suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = min(suffix[i + 1], nums[i])
        
        # Calculate the sum of beauties
        total_beauty = 0
        for i in range(1, n - 1):
            if prefix[i - 1] < nums[i] < suffix[i + 1]:
                total_beauty += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                total_beauty += 1
        
        return total_beauty