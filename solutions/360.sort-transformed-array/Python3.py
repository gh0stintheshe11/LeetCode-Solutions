from typing import List

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def f(x):
            return a * x * x + b * x + c
        
        n = len(nums)
        result = [0] * n
        i, j = 0, n - 1
        index = n - 1 if a > 0 else 0
        
        while i <= j:
            if a > 0:
                if f(nums[i]) > f(nums[j]):
                    result[index] = f(nums[i])
                    i += 1
                else:
                    result[index] = f(nums[j])
                    j -= 1
                index -= 1
            else:
                if f(nums[i]) < f(nums[j]):
                    result[index] = f(nums[i])
                    i += 1
                else:
                    result[index] = f(nums[j])
                    j -= 1
                index += 1
        
        return result