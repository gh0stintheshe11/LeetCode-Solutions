from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_arithmetic(arr: List[int]) -> bool:
            arr.sort()
            diff = arr[1] - arr[0]
            return all(arr[i+1] - arr[i] == diff for i in range(1, len(arr) - 1))
        
        result = []
        for start, end in zip(l, r):
            result.append(is_arithmetic(nums[start:end+1]))
        
        return result