class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even_indices = sorted(nums[i] for i in range(0, len(nums), 2))
        odd_indices = sorted((nums[i] for i in range(1, len(nums), 2)), reverse=True)
        
        result = []
        i, j = 0, 0
        
        for k in range(len(nums)):
            if k % 2 == 0:
                result.append(even_indices[i])
                i += 1
            else:
                result.append(odd_indices[j])
                j += 1
                
        return result