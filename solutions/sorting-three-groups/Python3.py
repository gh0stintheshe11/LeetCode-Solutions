from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Count number of 1's, 2's and 3's from the end
        count1, count2, count3 = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            count1[i] = count1[i + 1] + (nums[i] == 1)
            count2[i] = count2[i + 1] + (nums[i] == 2)
            count3[i] = count3[i + 1] + (nums[i] == 3)

        min_operations = float('inf')

        # Try every position to divide into groups
        count1_part = 0
        for i in range(n + 1):
            count2_part = 0
            for j in range(i, n + 1):
                # Remove non-1's before i, non-2's between i and j, non-3's after j
                operations = (i - count1_part) + (j - i - count2_part) + (n - j - count3[j])
                min_operations = min(min_operations, operations)
                
                if j < n and nums[j] == 2:
                    count2_part += 1
            
            if i < n and nums[i] == 1:
                count1_part += 1
        
        return min_operations