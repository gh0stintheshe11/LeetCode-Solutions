from typing import List

class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        # Split nums and target into odds and evens, and sort them
        nums_odd = sorted(x for x in nums if x % 2)
        nums_even = sorted(x for x in nums if x % 2 == 0)
        target_odd = sorted(x for x in target if x % 2)
        target_even = sorted(x for x in target if x % 2 == 0)

        operations = 0
        
        # Calculate the number of operations to make the odds similar
        for i in range(len(nums_odd)):
            if nums_odd[i] < target_odd[i]:
                operations += (target_odd[i] - nums_odd[i]) // 2

        # Calculate the number of operations to make the evens similar
        for i in range(len(nums_even)):
            if nums_even[i] < target_even[i]:
                operations += (target_even[i] - nums_even[i]) // 2

        return operations