from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)
        
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            
            low = 2
            high = 2 * limit
            
            diff[low] += 2
            diff[high + 1] -= 2
            
            diff[min(a, b) + 1] -= 1
            diff[max(a, b) + limit + 1] += 1
            
            diff[a + b] -= 1
            diff[a + b + 1] += 1
        
        min_moves = float('inf')
        current_moves = 0
        
        for x in range(2, 2 * limit + 1):
            current_moves += diff[x]
            min_moves = min(min_moves, current_moves)
        
        return min_moves