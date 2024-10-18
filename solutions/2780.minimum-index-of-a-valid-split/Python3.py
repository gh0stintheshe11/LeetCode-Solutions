class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Find the dominant element
        total_count = {}
        for num in nums:
            if num in total_count:
                total_count[num] += 1
            else:
                total_count[num] = 1
        
        dominant, freq = None, 0
        for num, count in total_count.items():
            if count * 2 > n:
                dominant = num
                freq = count
                break
        
        if dominant is None:
            return -1
        
        left_count = 0
        for i in range(n - 1):
            if nums[i] == dominant:
                left_count += 1
            
            right_count = freq - left_count
            
            if left_count * 2 > (i + 1) and right_count * 2 > (n - i - 1):
                return i
        
        return -1