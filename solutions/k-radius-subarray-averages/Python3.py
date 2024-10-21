class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avgs = [-1] * n
        if k == 0:
            return nums

        window_sum = 0
        window_size = 2 * k + 1
        
        if window_size > n:
            return avgs
        
        for i in range(window_size - 1):
            window_sum += nums[i]
        
        for i in range(k, n - k):
            window_sum += nums[i + k]
            avgs[i] = window_sum // window_size
            window_sum -= nums[i - k]

        return avgs