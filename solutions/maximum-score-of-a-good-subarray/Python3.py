class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = k, k
        min_val = nums[k]
        max_score = min_val
        
        while left > 0 or right < n - 1:
            if (left > 0 and right < n - 1):
                if nums[left - 1] > nums[right + 1]:
                    left -= 1
                else:
                    right += 1
            elif left > 0:
                left -= 1
            else:
                right += 1
                
            min_val = min(min_val, nums[left], nums[right])
            max_score = max(max_score, min_val * (right - left + 1))
        
        return max_score