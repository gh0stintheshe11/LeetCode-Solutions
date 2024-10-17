class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        x = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                x = i
            else:
                break
        if x == n - 1:
            return n * (n + 1) // 2
        y = n - 1
        for j in range(n - 1, 0, -1):
            if nums[j] > nums[j - 1]:
                y = j - 1
            else:
                break
        
        res = x + 1 + n - y
        j = bisect.bisect_right(nums[y:], nums[0]) + y
        res += n - j
        for i in range(1, x + 1):
            curr = nums[i]
            while j < n and nums[j] <= curr:
                j += 1
            if j == n: break
            res += n - j
            
        return res + 1