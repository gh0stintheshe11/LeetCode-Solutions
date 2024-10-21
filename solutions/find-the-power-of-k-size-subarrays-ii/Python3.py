class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * (len(nums) - k + 1)
        fail_at = 0
        for j in range(k-1, 0, -1):
            if nums[j]-1 != nums[j-1]:
                fail_at = j
                break
        
        for i in range(len(res)):
            if nums[i+k-1] - 1 != nums[i+k-2]:
                fail_at = i+k-1
            
            if i >= fail_at:
                res[i] = nums[i+k-1]
        
        return res