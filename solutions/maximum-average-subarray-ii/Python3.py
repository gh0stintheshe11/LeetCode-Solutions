class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def canFindLargerAverage(average: float) -> bool:
            min_prefix_sum = 0
            prefix_sum = 0
            curr_sum = 0
            for i in range(k):
                curr_sum += nums[i] - average
            if curr_sum >= 0:
                return True
            for i in range(k, len(nums)):
                curr_sum += nums[i] - average
                prefix_sum += nums[i - k] - average
                min_prefix_sum = min(min_prefix_sum, prefix_sum)
                if curr_sum >= min_prefix_sum:
                    return True
            return False
        
        left, right = min(nums), max(nums)
        precision = 1e-5
        while right - left > precision:
            mid = (left + right) / 2
            if canFindLargerAverage(mid):
                left = mid
            else:
                right = mid
        return left