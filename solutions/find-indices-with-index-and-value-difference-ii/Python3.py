class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        i = 0
        while i < len(nums): 
            while i < len(nums) and nums[i] < valueDifference:
                i+=1
            if i == len(nums):
                break
            j = 0
            while j <= i - indexDifference:
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i,j]
                j+=1
            j = i + indexDifference
            while j < len(nums):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i,j]
                j+=1
            i+=1
        return [-1,-1]