from typing import List

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        total_ones = sum(nums)
        max_score = 0
        best_indices = []

        count_zeros = 0
        count_ones = total_ones
        
        for i in range(len(nums) + 1):
            score = count_zeros + count_ones
            if score > max_score:
                max_score = score
                best_indices = [i]
            elif score == max_score:
                best_indices.append(i)
            
            if i < len(nums):
                if nums[i] == 0:
                    count_zeros += 1
                else:
                    count_ones -= 1
        
        return best_indices